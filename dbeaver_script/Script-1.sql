/* creation de l'utilisateur NSviattseva */
create user nsviattseva with encrypted password "qa12345678";

/* attribution de droits de super utilisateur a nsviattseva */
-- alter = modification
alter role nsviattseva superuser createdb createrole inherit login;
grant all privileges on database postgres to nsviattseva

alter user nsviattseva with password 'qa12345678';

/* creation de la base db_greta78 (par le super utilisateur postgres) */
create database db_greta78;

create database db_greta78;

create table tb_centre
( id serial primary key
, ville varchar(32)
);

insert into tb_centre (ville)
values
  ('Guyancourt')
, ('St-Germain')
, ('Plaisir')
, ('Acheres')
;
select * from tb_centre;

drop table if exists tb_matiere cascade;

create table tb_matiere
(id serial primary key
, intitule varchar(32)
, id_centre int
, constraint fk_centre foreign key (id_centre) references tb_centre (id)
);

insert into tb_matiere (intitule, id_centre)
values
  ('java', 1)
, ('python', 2)
, ('SQL', 2)
, ('Django', 2)
, ('RedactionCV', 2)
, ('Anglais', 1)
, ('BigData', 2)
, ('HTML', 3)
;

select * from tb_matiere;

insert into tb_matiere (intitule, id_centre)
values ('Francais', 3);

delete from tb_matiere
where intitule = 'Francais';

truncate tb_matiere;

select 
  tbM.intitule as matiere
, tbC.ville as centre
from tb_matiere as tbM, tb_centre as tbC
where tbM.id_centre = tbC.id 
order by centre; 

select 
  tbM.intitule as matiere
, tbC.ville as centre
from tb_matiere tbM
inner join tb_centre tbc
on tbM.id_centre = tbC.id 
order by 2 desc, 1 desc;

select 
  tbM.intitule as matiere
, tbC.ville as centre
from tb_matiere tbM
left join tb_centre tbc
on tbM.id_centre = tbC.id 
order by matiere;

select 
  tbM.intitule as matiere
, tbC.ville as centre
from tb_matiere tbM
right join tb_centre tbc
on tbM.id_centre = tbC.id 
order by matiere;

select 
  tbM.intitule as matiere
, tbC.ville as centre
from tb_matiere tbM
full join tb_centre tbc
on tbM.id_centre = tbC.id 
order by centre;

select * from tb_matiere;

create sequence tb_matiere restart 1;
drop sequence tb_matiere cascade;

drop table tb_matiere;

drop table if exists tb_formateur;

create table tb_formateur 
( id serial primary key
, nom varchar(32)
, prenom varchar(32)
);

select * from tb_formateur;

alter table tb_formateur 
add column id_matiere int;

alter table tb_formateur 
add constraint fk_centre foreign key (id_matiere) references tb_matiere (id);

insert into tb_formateur (nom, prenom, id_matiere)
values
  ('VERONIE', 'Gilles', 2)
, ('MARTIN', 'Guy', 1)
, ('AMAR', 'JMichel', 3)
, ('De BORREDON', 'Estelle', 5)
, ('KNOX', 'David', 6)
, ('LIMA', 'Alex', null)
;

insert into tb_formateur (nom, prenom, id_matiere)
values
  ('BOUZID', 'Samir', null)
;

update tb_formateur 
set prenom = 'Gilles'
where id = '1';

delete from tb_formateur where id=8;

select * from tb_formateur where id in (1,2);

select * from tb_formateur where id between 2 and 5;

select 
  tbF.id as id_formateur
, tbF.nom
, tbF.prenom
, tbM.intitule as matiere
from tb_formateur tbF
full join tb_matiere tbM
on tbF.id_matiere = tbM.id
order by matiere;

select 
  tbF.*
, tbM
from tb_formateur as tbF
full join tb_matiere as tbm 
on tbF.id_matiere = tbM.id;

select * from tb_formateur 
select * from tb_matiere
select * from tb_centre

select 
  tbF.id as id_formateur
, tbF.nom
, tbF.prenom
, tbM.intitule as matiere
, tbC.ville as centre
from tb_formateur tbF
full  join tb_matiere tbM on tbF.id_matiere = tbM.id
full  join tb_centre tbC on tbM.id_centre = tbc.id 
order by matiere;

drop table if exists tb_apprenant cascade;

create table tb_apprenant
( id serial primary key
, nom varchar(32)
, prenom varchar(32)
, id_matiere int
, constraint fk_matiere foreign key (id_matiere) references tb_matiere (id)
);

insert into tb_apprenant (nom, prenom, id_matiere)
values
  ('ABITBOL', 'Franck', 2)
, ('BELAA', 'Adlane', 3)
, ('HOUNDJREBO', 'Cornelia', 5)
, ('MASSET', 'Benjamin', 4)
, ('MASSE', 'Felix', 3)
, ('NDIAYE', 'Aminata', 4)
, ('OUADA', 'Mohamed', 2)
, ('SAGNA', 'Daouda', 1)
, ('SETKH', 'Elizaveta', 2)
, ('SVIATTSEVA', 'Natalia', 4)
, ('USUI', 'Katsuji', 1)
;

select * from tb_apprenant;

select * from tb_apprenant where nom like 'M%';

select * from tb_apprenant where prenom like '%a%';

select * from tb_apprenant where prenom like '%a%' or prenom like '%A%';

select 
  tbA.nom
, tbA.prenom
, tbM.intitule as matiere
, tbC.ville as centre
, tbF.nom as nom_formateur
, tbF.prenom as prenom_formateur
from tb_apprenant tbA
full  join tb_formateur tbF on tbA.id_matiere = tbF.id_matiere
full  join tb_matiere tbM on tbF.id_matiere = tbM.id
full  join tb_centre tbC on tbM.id_centre = tbc.id 
order by matiere;

insert into tb_apprenant (nom, prenom) values ('SAPRITCH', 'Alice');

select * from tb_apprenant where id between 4 and 8;

select 
  tbA.nom
, tbA.prenom
, tbM.intitule as matiere
from tb_apprenant tbA
left join tb_matiere tbM on tbA.id_matiere = tbM.id
order by matiere;

insert into tb_apprenant (nom, prenom) values ('SAPRITCH', 'alice');

select 
  tbA.id as id_apprenant
, tbA.nom
, tbA.prenom
, tbM.intitule as matiere
from tb_apprenant tbA
full outer join tb_matiere tbm 
on tbA.id_matiere = tbM.id 
order by id_apprenant, id_matiere;

delete 
from tb_apprenant tb1
using tb_apprenant tb2
where tb1.id > tb2.id
and tb1.nom = tb2.nom
and tb1.prenom = tb2.prenom
;

select * from tb_apprenant;

-- ajout d'une clé unique sur la table portant tb_formateur sur le nom et prénom
create unique index on tb_formateur (nom, prenom);

ALTER TABLE tb_formateur
ADD CONSTRAINT ui_formateur unique (nom, prenom);

select * from tb_formateur;

insert into tb_formateur (nom, prenom) values 
  ('BOUZID', 'Samir')
, ('LIMA', 'Alex')
;

alter table tb_formateur 
drop constraint ui_formateier;

-- comptage du nombre d'apprenants
select count(*) as nb_apprenants from tb_apprenant;

-- selection des apprenants par matiere
select 
  tbM.id as id_matiere
, tbM.intitule as matiere
, count(tbA.id) as nb_apprenants
from tb_matiere tbM
left join tb_apprenant tbA
on tbM.id = tbA.id_matiere
group by tbM.id, tbM.intitule
order by id_matiere;

select 
  tbM.id as id_matiere
, tbM.intitule as matiere
, count(tbA.id) as nb_apprenants
from tb_matiere tbM
left join tb_apprenant tbA
on tbM.id = tbA.id_matiere
group by tbM.id, tbM.intitule
order by id_matiere;

select 
  max(nb_max) as max_apprenants
from (select 
      max(nb_apprenants) as nb_max
      from (select
      		  tbM.id as id_matiere
      		, tbM.intitule as matiere
      		, count(tbA.id) as nb_apprenants 
      		from tb_matiere tbM
      		left join tb_apprenant tbA 
      		on tbM.id = tbA.id_matiere
      		group by tbM.id, tbM.intitule
      		) as tb1
      	group by id_matiere, matiere
      	) as tb2
;

select 
    tb3.intitule,
    tb2.maximum_apprenants 
    from     (select 
                    max(tb1.nb_apprenants) as maximum_apprenants 
                    from (
                    select     tm.intitule, 
                        count (distinct ta.id) as nb_apprenants
                        from tb_matiere tm 
                        left join tb_apprenant ta on tm.id = ta.id_matiere 
                        group by tm.intitule) as tb1
            ) as tb2
            inner join 
             (select
                     tm.intitule, 
                    count (distinct ta.id) as nb_apprenants
                    from tb_matiere tm 
                    left join tb_apprenant ta on tm.id = ta.id_matiere 
                    group by tm.intitule) as tb3
            on tb2.maximum_apprenants = tb3.nb_apprenants;
           
-- selection de la matiere qui a le plus grand nombre d'apprenants
--           utilisation de la clase with
with tb1 as
( select
	tbM.id as id_matiere
  ,	tbM.intitule as matiere
  , count(tbA.id) as nb_apprenants
  from tb_matiere tbM
  left join tb_apprenant tbA 
  on tbM.id = tbA.id_matiere
  group by tbM.id, tbM.intitule
)
,
tb2 as 
( select
  max(nb_apprenants) as nb_max
  from tb1
)
select
  tb1.id_matiere
, tb1.matiere
, tb2.nb_max as max_apprenants
from tb1, tb2
where tb1.nb_apprenants = tb2.nb_max
;

select * from tb_apprenant 

alter table tb_apprenant 
add age_apprenant int;

update tb_apprenant set age_apprenant='30' where prenom='Franck';
update tb_apprenant set age_apprenant='39' where prenom='Adlane';
update tb_apprenant set age_apprenant='38' where prenom='Cornelia';
update tb_apprenant set age_apprenant='37' where prenom='Benjamin';
update tb_apprenant set age_apprenant='36' where prenom='Felix';
update tb_apprenant set age_apprenant='35' where prenom='Aminata';
update tb_apprenant set age_apprenant='34' where prenom='Mohamed';
update tb_apprenant set age_apprenant='33' where prenom='Daouda';
update tb_apprenant set age_apprenant='32' where prenom='Elizaveta';
update tb_apprenant set age_apprenant='31' where prenom='Natalia';
update tb_apprenant set age_apprenant='30' where prenom='Katsuji';
update tb_apprenant set age_apprenant='29' where prenom='Alice';

select avg(age_apprenant) from tb_apprenant;
select round(avg(age_apprenant), 2) from tb_apprenant;

-- selection des personnes enregistés dans db_greta78
-- utilisation de la clause d'agrégat union
select 
  nom
, prenom 
, 'formateur' as qualite
from tb_formateur 
union
select 
  nom
, prenom 
, 'apprenant' as qualite
from tb_apprenant
order by nom, prenom
;

-- selection des personnes affectés à un centre
-- utilisation des clauses with et union
with 
tb1 as
( select 
    coalesce(tbC.ville, '-inconnu-') as centre
  , tbF.nom
  , tbF.prenom
  , 'formateur' as qualite
  , coalesce(tbM.intitule, '-inconnu-') as matiere
  from tb_formateur tbF
  left join tb_matiere tbM 
  on tbM.id = tbF.id_matiere
  left join tb_centre tbC 
  on tbC.id = tbM.id_centre
  order by centre, qualite desc, nom asc
),
tb2 as
( select 
    coalesce(tbC.ville, '-inconnu-') as centre
  , tbA.nom
  , tbA.prenom
  , 'apprenant' as qualite
  , coalesce(tbM.intitule, '-inconnu-') as matiere
  from tb_apprenant tbA
  left join tb_matiere tbM 
  on tbM.id = tbA.id_matiere
  left join tb_centre tbC 
  on tbC.id = tbM.id_centre
  order by centre, qualite desc, nom asc
)
select * from tb1 
union
select * from tb2
order by centre, qualite desc, nom asc
;


select * from tb_formateur 
select * from tb_matiere
select * from tb_centre
select * from tb_apprenant 

with 
tb1 as
( select 
    coalesce(tbC.ville, '-inconnu-') as centre
  , tbF.nom
  , tbF.prenom
  , 'formateur' as qualite
  , coalesce(tbM.intitule, '-inconnu-') as matiere
  from tb_formateur tbF
  left join tb_matiere tbM 
  on tbM.id = tbF.id_matiere
  left join tb_centre tbC 
  on tbC.id = tbM.id_centre
  order by centre, qualite desc, nom asc
),
tb2 as
( select 
    coalesce(tbC.ville, '-inconnu-') as centre
  , tbA.nom
  , tbA.prenom
  , 'apprenant' as qualite
  , coalesce(tbM.intitule, '-inconnu-') as matiere
  from tb_apprenant tbA
  left join tb_matiere tbM 
  on tbM.id = tbA.id_matiere
  left join tb_centre tbC 
  on tbC.id = tbM.id_centre
  order by centre, qualite desc, nom asc
),
tb3 as 
( select * from tb1 
  union
  select * from tb2
  order by centre, qualite desc, nom asc
)
select 
  centre
, count(*) as nb_personnels
from tb3
group by centre
order by centre;

with 
tb1 as
( select 
    coalesce(tbC.ville, '-inconnu-') as centre
  , tbF.nom
  , tbF.prenom
  , 'formateur' as qualite
  , coalesce(tbM.intitule, '-inconnu-') as matiere
  from tb_formateur tbF
  left join tb_matiere tbM 
  on tbM.id = tbF.id_matiere
  left join tb_centre tbC 
  on tbC.id = tbM.id_centre
  order by centre, qualite desc, nom asc
),
tb2 as
( select 
    coalesce(tbC.ville, '-inconnu-') as centre
  , tbA.nom
  , tbA.prenom
  , 'apprenant' as qualite
  , coalesce(tbM.intitule, '-inconnu-') as matiere
  from tb_apprenant tbA
  left join tb_matiere tbM 
  on tbM.id = tbA.id_matiere
  left join tb_centre tbC 
  on tbC.id = tbM.id_centre
  order by centre, qualite desc, nom asc
)
 select * from tb1 
  union
  select * from tb2
  order by centre, qualite desc, nom asc;
  
with tb1 as 
( select tf.nom, 
        tf.prenom,
        'formateur' as role,
        coalesce(tm.intitule, 'inconnue') as matiere,
        coalesce(tc.ville, 'inconnue') as ville
        from tb_formateur tf
                    left join tb_matiere tm on tf.id_matiere = tm.id
                    left join tb_centre tc on tm.id_centre = tc.id),
tb2 as 
(select ta.nom, 
        ta.prenom,
        'apprenant' as role,
        coalesce(tm.intitule, 'inconnue') as matiere,
        coalesce(tc.ville, 'inconnue') as ville
        from tb_apprenant ta 
                    left join tb_matiere tm on ta.id_matiere = tm.id
                    left join tb_centre tc on tm.id_centre = tc.id),
tb3 as 
(select * from tb1 union select * from tb2),
tb4 as 
(select 
    ville,
    count (*) as nb_personnes
    from tb3
group by ville),
tb5 as 
(select 
    max(nb_personnes) as max_personnes
    from tb4)
select tb4.ville,tb5.max_personnes
    from tb4 inner join tb5 on tb4.nb_personnes = tb5.max_personnes;
    
create table tb_apprenant_matiere
( id_apprenant int
, id_matiere int
, constraint pk_apprenant_matiere primary key (id_apprenant, id_matiere)
, constraint fk_apprenant foreign key (id_apprenant) references tb_apprenant (id)
, constraint fk_matiere foreign key (id_matiere) references tb_matiere (id)
);

insert into tb_apprenant_matiere (id_apprenant, id_matiere)
values
 (1,3),(1,5)
,(2,1),(2,3)
,(3,2),(3,5)
,(4,1)
,(5,3),(5,5)
,(6,1),(6,3)
,(7,2),(7,5)
,(8,1),(8,2),(8,4)
,(9,2),(9,6)
,(10,3)
,(11,1),(11,6)
;

select * from tb_formateur 
select * from tb_matiere
select * from tb_centre
select * from tb_apprenant 
select * from tb_apprenant_matiere


--select distinct 

select
  case 
    when tbA.id is null then 0
    else tbA.id
  end as id_apprenant
, case 
	when tbA.nom is null then '??'
	else tbA.nom
  end
, case 
	when tbA.prenom is null then '??'
	else tbA.prenom
  end
, coalesce(tbM.id, 0) as id_matiere
, coalesce(tbM.intitule, '??') as matiere
from tb_apprenant tbA 
left join tb_apprenant_matiere tbAM 
on tbA.id = tbAM.id_apprenant
left join tb_matiere tbM 
on tbAM.id_matiere = tbM.id 
order by 1, 4;

select  ta.id,
        ta.nom, 
        ta.prenom,
        ta.age_apprenant,
        tm.intitule,
        case 
            when tm.intitule in ('SQL','Django','Java','Python') then 'Informatique'
            when tm.intitule in ('RedactionCV','Anglais') then 'Autres'
        end as type_matiere
    from tb_apprenant_matiere tam     left join tb_apprenant ta on tam.id_apprenant = ta.id  
                                    left join tb_matiere tm on tam.id_matiere = tm.id  ;
  
                                   
select
  case 
    when tbA.id is null then 0
    else tbA.id
  end as id_apprenant
, case 
	when tbA.nom is null then '??'
	else tbA.nom
  end
, case 
	when tbA.prenom is null then '??'
	else tbA.prenom
  end
, coalesce(tbM.id, 0) as id_matiere
, coalesce(tbM.intitule, '??') as matiere
from tb_apprenant tbA 
full join tb_apprenant_matiere tbAM 
on tbA.id = tbAM.id_apprenant
full join tb_matiere tbM 
on tbAM.id_matiere = tbM.id 
order by 1, 4;

alter table tb_apprenant
drop constraint fk_matiere;

alter table tb_apprenant
drop column id_metiere;

select * from tb_formateur, tb_matiere

create table tb_formateur_matiere
( id_formateur int
, id_matiere int
, constraint pk_formateur_matiere primary key (id_formateur, id_matiere)
, constraint fk_formateur foreign key (id_formateur) references tb_formateur (id)
, constraint fk_matiere foreign key (id_matiere) references tb_matiere (id)
);

insert into tb_formateur_matiere (id_formateur, id_matiere)
values
 (1,3),(1,5)
,(2,1),(2,3)
,(3,2),(3,5)
,(4,1)
,(5,3),(5,5)
,(6,1),(6,3)
,(7,2),(7,5)
;

select * from tb_formateur 
select * from tb_matiere
select * from tb_centre
select * from tb_apprenant 
select * from tb_apprenant_matiere
select * from tb_formateur_matiere

select
  case 
    when tbF.id is null then 0
    else tbF.id
  end as id_formateur
, case 
	when tbF.nom is null then '??'
	else tbF.nom
  end
, case 
	when tbF.prenom is null then '??'
	else tbF.prenom
  end
, coalesce(tbM.id, 0) as id_matiere
, coalesce(tbM.intitule, '??') as matiere
from tb_formateur tbF
full join tb_formateur_matiere tbFM 
on tbF.id = tbFM.id_formateur
full join tb_matiere tbM 
on tbFM.id_matiere = tbM.id 
order by 1, 4;

alter table tb_formateur
drop column id_metiere;

alter table tb_apprenant
drop constraint fk_matiere;

/* création de la vue apprenants metiere */
drop view if exists vw_apprenant_matiere;

create view vw_apprenant_matiere as
select
  case when tbA.id is null then 0 else tbA.id end as id_apprenant,
  case when tbA.nom is null then '??' else tbA.nom end,
  case when tbA.prenom is null then '??' else tbA.prenom end,
  coalesce(tbM.id, 0) as id_matiere,
  coalesce(tbM.intitule, '??') as matiere
from
  tb_apprenant tbA
  left join tb_apprenant_matiere tbAM on tbAM.id_apprenant = tbA.id
  left join tb_matiere tbM on tbAM.id_matiere = tbM.id
order by 1, 4;

select * from vw_apprenant_matiere;

/* création de la vue matiere apprenant*/
drop view if exists vw_matiere_apprenant;

create view vw_matiere_apprenant as
select
  case when tbM.id is null then 0 else tbM.id end as id_matiere,
  case when tbM.intitule is null then '??' else tbM.intitule end as matiere,
  coalesce(tbA.id, 0),
  coalesce(tbA.nom, '??') as nom,
  coalesce(tbA.prenom, '??') as prenom
from
  tb_matiere tbM
  left join tb_apprenant_matiere tbAM on tbAM.id_matiere = tbM.id
  left join tb_apprenant tbA on tbAM.id_apprenant = tbA.id
order by 1, 3;
 
select * from vw_matiere_apprenant;

/* création de la vue formateur matiere */
drop view if exists vw_formateur_matiere;

create view vw_formateur_matiere as
select
  case when tbF.id is null then 0 else tbF.id end as id_formateur,
  case when tbF.nom is null then '??' else tbF.nom end,
  case when tbF.prenom is null then '??' else tbF.prenom end,
  coalesce(tbM.id, 0) as id_matiere,
  coalesce(tbM.intitule, '??') as matiere
from
  tb_formateur tbF
  left join tb_formateur_matiere tbFM on tbFM.id_formateur = tbF.id
  left join tb_matiere tbM on tbFM.id_matiere = tbM.id
order by 1, 4;

select * from vw_formateur_matiere;

/* création de la vue matiere formateur*/
drop view if exists vw_matiere_formateur;

create view vw_matiere_formateur as
select
  case when tbM.id is null then 0 else tbM.id end as id_matiere,
  case when tbM.intitule is null then '??' else tbM.intitule end as matiere,
  coalesce(tbF.id, 0) as id_formateur,
  coalesce(tbF.nom, '??') as nom,
  coalesce(tbF.prenom, '??')as prenom
from
  tb_matiere tbM
  left join tb_formateur_matiere tbFM on tbFM.id_matiere = tbM.id
  left join tb_formateur  tbF on tbFM.id_formateur = tbF.id
order by 1;
 
select * from vw_matiere_formateur;

-----------------------------------------------------------------------------

`
-----------------------------------------------------------------------------------------

/** fonctions & triggers **/

/* selection de la liste de contenants (tables & vues) de la base greta */
select * from information_schema.tables;

/* selection de la liste des champs de la table tb_formateur */
select * from information_schema.columns where table_name = 'tb_formateur';

select column_name, data_type from information_schema.columns where table_name = 'tb_formateur';


/* creation d'une fonction de formatage de la date du jour */
drop function if exists fx_today();

create function fx_today()
returns varchar(40) language plpgsql as
$$
declare aujourdhui varchar(64);

begin
	select now() into aujourdhui;
--	return(format(aujourdhui), 'DD-MM-YYYY HH:MI');
	return ( to_char(current_timestamp, 'DD/MM/YYYY HH:MI'));
end;
$$

select now();
select current_timestamp;
select fx_today();

select localtimestamp(0); 

/* creation de la table tb_audit */
drop table if exists tb_audit;
create table db_audit
( id serial primary key 
, id_apprenant int not null
, mouvement varchar(32)
, date_mouvement varchar(64)
);

select * from tb_audit;

/* creation d'une fonction d'insertion de données dans la table tb_audit */
drop function if exists fx_apprenant_insert() cascade;
create function fx_apprenant_insert() 
returns trigger language plpgsql as
$$
declare 
 mouvement_date varchar(64);
 ok boolean;
begin 
	select localtimestamp(0) into mouvement_date;
	insert into tb_audit (id_apprenant, mouvement, date_mouvement)
	values (new.id, 'inscription', mouvement_date);
	boolean ok;
end;
$$

/* creation d'un trigger d'insertion automatique de données dans la table tb_audit
aprés d'insertion d'un nouvel apprenant dans la table tb_apprenant */
drop trigger if exists tg_apprenant_insert on tb_apprenant;
create trigger tg_apprenant_insert
after insert on tb_apprenant
for each row execute procedure fx_apprenant_insert();

insert into tb_apprenant (nom, prenom)
values ('DURAND', 'Rafael')

select * from tb_apprenant;
select * from tb_audit;

