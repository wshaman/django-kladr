+insert into kladr_region
  (code,name, socr, index,gninmb,uno,ocatd,status)
  select code,name, socr, index,gninmb,uno,ocatd,status
    from kladr
    where code like '%000000000__';

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
--create or replace function regionid(IN r TEXT)
--	RETURNS CHARACTER VARYING(20) as $$
--	DECLARE t CHARACTER VARYING(20);
--	BEGIN
--		select overlay(r placing repeat('0',char_length(r)-4) from 3 ) into t;
--                RETURN t;
--        END;
--$$ LANGUAGE plpgsql;
--
--create or replace function regionfid(IN r TEXT)
--	RETURNS CHARACTER VARYING(20) as $$
--	DECLARE t CHARACTER VARYING(20);
--	BEGIN
--		select newcode from altnames into t where oldcode=r;
--		select COALESCE(t,r) into r;
--		select overlay(r placing repeat('0',char_length(r)-4) from 3 ) into t;
--                RETURN t;
--        END;
--$$ LANGUAGE plpgsql;
--
--create or replace function districtid(IN r TEXT)
--	RETURNS CHARACTER VARYING(20) as $$
--	DECLARE t CHARACTER VARYING(20);
--	BEGIN
--		select overlay(r placing repeat('0',char_length(r)-7) from 6 ) into t;
--                RETURN t;
--        END;
--$$ LANGUAGE plpgsql;
--
--create or replace function districtfid(IN r TEXT)
--	RETURNS CHARACTER VARYING(20) as $$
--	DECLARE t CHARACTER VARYING(20);
--	BEGIN
--		select newcode from altnames into t where oldcode=r;
--		select COALESCE(t,r) into r;
--		select overlay(r placing repeat('0',char_length(r)-7) from 6 ) into t;
--                RETURN t;
--        END;
--$$ LANGUAGE plpgsql;
--
--
--
--INSERT INTO kladr_region
--	(code,name, socr, index,gninmb,uno,ocatd,status)
--	select regionid(code) as code,name, socr, index,gninmb,uno,ocatd,status
--		from kladr
--		where code like '%000000000__';
--
--INSERT INTO kladr_district
--	(code,name, socr, index,gninmb,uno,ocatd,status,region_id)
--	select districtid(code) as code,
--	name, socr, index,gninmb,uno,ocatd,status, regionfid(code) as region_id
--			from kladr
--			where not code like '%000000000__'
--			and code like '%000000__'
--			and code like '55%'
--INSERT INTO kladr_city
--	(code,name, socr, index,gninmb,uno,ocatd,status,region_id,district_id)
--	select cityid(code) as code,
--	name, socr, index,gninmb,uno,ocatd,status, regionfid(code) as region_id, districtfid(code) as district_id
--			from kladr
--			where not code like '%000000__'
--			and code like '%000__'
--			and code like '55%'
--			and substr(code,1,5) not like '%000';
--INSERT INTO kladr_city
--	(code,name, socr, index,gninmb,uno,ocatd,status,region_id,district_id)
--	select cityid(code) as code,
--	name, socr, index,gninmb,uno,ocatd,status, regionfid(code) as region_id, null as district_id
--			from kladr
--			where not code like '%000000__'
--			and code like '%000__'
--			and code like '55%'
--			and substr(code,1,5) like '%000';
