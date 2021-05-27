select taxon, default_color, max(n)
from (
    select taxon, value as default_color, count(*) as n
    from traits
    join fields using (trait_id)
    where field = 'color'
    group by taxon, default_color
)
group by taxon;