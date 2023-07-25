select firstName, lastName, city, state
from person as p left join address as a
on p.personId = a.personId;