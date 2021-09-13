const ENDPOINT = 'https://sfg.taxonworks.org/api/v1/taxon_names';
const PROJECT = 'project_token=iu4ty6tOdWg_-cceoQjhyQ';
const ODONATA = 'taxon_name_id=707405';
const PER = 'per=10000'; // Get them all in a single request
const DESC = 'descendants=true';
const GROUP = 'nomenclature_group=Species';
const URL = `${ENDPOINT}?${PROJECT}&${ODONATA}&${DESC}&${GROUP}&${PER}`;

const TODAY = Utilities.formatDate(new Date(), 'GMT', 'yyyy-MM-dd');


function onOpen() {
    SpreadsheetApp.getUi()
        .createMenu('Taxon Works')
        .addItem('Check names', 'checkNames')
        .addItem('Check names (both ways)', 'checkNamesBothWays')
        .addToUi();
}


function checkNames() {
    updateTaxonWorksHeader();
    let species = getTaxonWorksSpecies();
    let tw_primary = buildPrimaryTable(species);
    let tw_secondary = buildSecondaryTable(tw_primary);
    notInTaxonWorks(tw_primary, tw_secondary);
    return tw_primary;
}


function checkNamesBothWays() {
    let tw_primary = checkNames();
    notInCheckList(tw_primary);
}


function updateTaxonWorksHeader() {
    const taxonWorksCol = getTaxonWorksColumn();
    const sheet = SpreadsheetApp.getActiveSheet();
    const range = sheet.getRange(1, taxonWorksCol);
    range.setValue(`Taxon Works (${TODAY})`);
}


function getGenusColumn() {
    const sheet = SpreadsheetApp.getActiveSheet();
    const lastCol = sheet.getLastColumn();
    const range = sheet.getRange(1, 1, 1, lastCol);
    const values = range.getValues()[0];

    var genusCol = -1;
    Object.values(values).forEach((val, i) => {
        if (genusCol == -1
            && val.toLowerCase() == 'genus'
            && values[i+1].toLowerCase() == 'species')
        {
            genusCol = i;
        }
    });
    if (genusCol == -1) {
      throw('Could not find the "GENUS" column.');
    }
    return genusCol + 1;
}


function getTaxonWorksColumn() {
    const sheet = SpreadsheetApp.getActiveSheet();
    const lastCol = sheet.getLastColumn();
    const range = sheet.getRange(1, 1, 1, lastCol);
    const values = range.getValues();

    var taxonWorksCol = -1;
    Object.values(values[0]).forEach((val, i) => {
        if (taxonWorksCol == -1
            && val.toLowerCase().startsWith('taxon works'))
        {
            taxonWorksCol = i;
        }
    });
    if (taxonWorksCol == -1) {
      throw('Could not find the "Taxon Works" column.');
    }
    return taxonWorksCol + 1;
}


function getTaxonWorksSpecies() {
    let jsonData = UrlFetchApp.fetch(URL);
    let species = JSON.parse(jsonData.getContentText())
        .filter(s => s.rank == 'species');
    species.forEach(s => s.matched = false);
    return species;
}


function buildPrimaryTable(species) {
    const tw_primary = {};
    species.forEach(rec => tw_primary[rec.cached] = rec);
    return tw_primary;
}


function buildSecondaryTable(tw_primary) {
    const tw_secondary = {};
    Object.values(tw_primary).forEach(rec => {
        tw_secondary[rec.cached_primary_homonym] = rec;
        tw_secondary[rec.cached_secondary_homonym] = rec;
    });
    return tw_secondary;
}


function notInTaxonWorks(tw_primary, tw_secondary) {
    const sheet = SpreadsheetApp.getActiveSheet();
    const last = sheet.getLastRow();
    const taxonWorksCol = getTaxonWorksColumn();
    const genusCol = getGenusColumn();

    const msg_range = sheet.getRange(2, taxonWorksCol, last - 1);
    msg_range.clear();

    const nameRange = sheet.getRange(2, genusCol, last - 1, 2);
    nameRange.getValues().forEach((raw, n) => {
        const row = n + 2;
        const name = `${raw[0]} ${raw[1]}`;
        if (tw_primary.hasOwnProperty(name)) {
            tw_primary[name].matched = true;
        } else if (tw_secondary.hasOwnProperty(name)) {
            tw_secondary[name].matched = true;
            const range = sheet.getRange(row, taxonWorksCol)
                .setValue(tw_secondary[name].name_string)
                .setBackground('yellow');
        } else if (name.length > 3) {
            const range = sheet.getRange(row, taxonWorksCol)
                .setValue('missing').setBackground('red');
        }
    });
}


function notInCheckList(tw_primary) {
    const sheet = SpreadsheetApp.getActiveSheet();
    const last = sheet.getLastRow();
    const taxonWorksCol = getTaxonWorksColumn();

    let missing = [];
    Object.values(tw_primary).filter(s => !s.matched)
        .filter(s => s.id == s.cached_valid_taxon_name_id)
        .filter(s => s.rank == 'species')
        .forEach(s => missing.push([s.name_string]));

    if (missing.length) {
        missing = missing.sort();
        const last = sheet.getLastRow();
        const range = sheet.getRange(last + 1, taxonWorksCol, missing.length);
        range.setValues(missing).setBackground('red');
    }
}
