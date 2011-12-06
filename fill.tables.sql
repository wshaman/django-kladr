insert into kladr_region
	(code,name, socr, index,gninmb,uno,ocatd,status)
	select code,name, socr, index,gninmb,uno,ocatd,status
		from kladr
		where code like '%000000000__';


insert into kladr_district
	(code,name, socr, index,gninmb,uno,ocatd,status)
	select code,name, socr, index,gninmb,uno,ocatd,status

			from kladr
			where not code like '%000000000__'
			and code like '%000000__';


insert into kladr_city
	(code,name, socr, index,gninmb,uno,ocatd,status)
	select code,name, socr, index,gninmb,uno,ocatd,status
		from kladr
		where not code like '%000000__'
		and code like '%000__'



insert into kladr_ville
	(code,name, socr, index,gninmb,uno,ocatd,status)
	select code, name, socr, index,gninmb,uno,ocatd,status

		from kladr
		where not code like '%000__'