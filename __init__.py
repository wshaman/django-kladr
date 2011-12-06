# -*- coding: utf-8 -*-
"""
@annotate: попытка автоматически создать полноценную базу со связями провалилась.
Вернусь к ней позже - соберу полноценный модуль джанго для работы с КЛАДРом.
Ниже заметки и наброски для себя на будущее
@author: serge <serge@shtripling.com>
"""
"""

#!!Ставим pgdbf, потом 2 заклинания в шеле.(подставить данные)
for i in $(ls |grep -i dbf$) ; do pgdbf $i |iconv -f 866 > $i.sql ; done
#for i in $(ls |grep sql$) ; do psql -h 192.168.0.142 -U postgres reestr_db < $i ; done
#for i in $(ls |grep sql$) ; do psql -h localhost -U postgres reestr_db < $i ; done

Таблички создаются из django, да-да
python manage.py syncdb
Теперь заполняем таблички:
запросы в fill.tables.sql
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