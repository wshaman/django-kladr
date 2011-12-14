# -*- coding: utf-8 -*-
"""
@annotate: попытка автоматически создать полноценную базу со связями провалилась.
Вернусь к ней позже - соберу полноценный модуль джанго для работы с КЛАДРом.
Ниже заметки и наброски для себя на будущее
@author: serge
"""
"""

#!!Ставим pgdbf, потом 2 заклинания в шеле.(подставить данные)
for i in $(ls |grep -i dbf$) ; do pgdbf $i |iconv -f 866 > $i.sql ; done
for i in $(ls |grep sql$) ; do psql -h 192.168.0.142 -U postgres reestr_db < $i ; done

Таблички создаются из django
ФОКУС!!! Альтернативные имена ломают всю логику
Теперь заполняем таблички:
BEGIN;
insert into kladr_region
	(code,name, socr, index,gninmb,uno,ocatd,status)
	select substr(code,1,2) as code,name, socr, index,gninmb,uno,ocatd,status
		from kladr
		where code like '%000000000__';


insert into kladr_district
	(code,name, socr, index,gninmb,uno,ocatd,status,region_id)
	select substr(code,1,5) as code,name, socr, index,gninmb,uno,ocatd,status, substr(code,1,2) as region_id

			from kladr
			where not code like '%000000000__'
			and code like '%000000__';

-- города записываем в 2 прохода - для кого существует запись в районе, и для прочих.
-- Для первых пишем null в поле района. UNION тут не лучше просто потому, что UNION
insert into kladr_city 
	(code,name, socr, index,gninmb,uno,ocatd,status,region_id,district_id)
	select substr(code,1,8) as code,name, socr, index,gninmb,uno,ocatd,status,
	substr(code,1,2) as region_id, null as district_id
		from kladr
		where not code like '%000000__'
		and code like '%000__'
		and substr(code,1,5) like '%000';
insert into kladr_city
	(code,name, socr, index,gninmb,uno,ocatd,status,region_id,district_id)
	select substr(code,1,8) as code,name, socr, index,gninmb,uno,ocatd,status,
	substr(code,1,2) as region_id, substr(code,1,5) as district_id
		from kladr
		where not code like '%000000__'
		and code like '%000__'
		and substr(code,1,5) not like '%000';


insert into kladr_ville
	(code,name, socr, index,gninmb,uno,ocatd,status,region_id,district_id,city_id)
	select substr(code,1,11) as code, name, socr, index,gninmb,uno,ocatd,status,
	substr(code,1,2) as region_id, substr(code,1,5) as district_id, substr(code,1,8) as city_id
		from kladr
		where not code like '%000__'
		and code like '%00'
		and substr(code,1,5) not like '%000'
		and substr(code,1,8) not like '%000';

COMMIT;

"""






"""
--00000000000000000
--0000000000000
--insert into kladr_region (select * from kladr where code like '%00000000000');
BEGIN;
insert into kladr_ville
	(code,name, socr, index,gninmb,uno,ocatd,status,region_id,district_id,city_id)
	select villeid(code) as code, name, socr, index,gninmb,uno,ocatd,status,
	regionfid(code) as region_id, districtfid(code) as district_id, cityfid(code) as city_id
		from kladr
		where not code like '%000__'
		and substr(code,1,5) not like '%000'
		and substr(code,1,8) not like '%000'
		and code like '55%'
	UNION
	select villeid(code) as code, name, socr, index,gninmb,uno,ocatd,status,
	regionfid(code) as region_id, null as district_id, cityfid(code) as city_id
		from kladr
		where not code like '%000__'
		and substr(code,1,5) like '%000'
		and substr(code,1,8) not like '%000'
		and code like '55%'
	UNION
	select villeid(code) as code, name, socr, index,gninmb,uno,ocatd,status,
	regionfid(code) as region_id, districtfid(code) as district_id, null as city_id
		from kladr
		where not code like '%000__'
		and substr(code,1,5) not like '%000'
		and substr(code,1,8) like '%000'
		and code like '55%'
	UNION
	select villeid(code) as code, name, socr, index,gninmb,uno,ocatd,status,
	regionfid(code) as region_id, null as district_id, null as city_id
		from kladr
		where not code like '%000__'
		and substr(code,1,5) like '%000'
		and substr(code,1,8) like '%000'
		and code like '55%';

COMMIT;
"""