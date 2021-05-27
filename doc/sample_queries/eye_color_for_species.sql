select *
from traits
join fields using (trait_id)
where field = 'color'
and part = 'eye'
and taxon like 'Calopteryx dimidiata'