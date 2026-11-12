select p.lastName,
p.firstName, a.city,
a.state from person p 
left join address a
on a.personId=p.personId
