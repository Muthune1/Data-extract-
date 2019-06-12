put file://C:\Users\muthu_000\Python3.7\work\out_3d.csv @my_int_Stage_csv;
create or replace table temp_pyadmob_rev_1 as select  $1,$2,$3,$4,$5,$6,$7,$8 from @my_int_stage_csv/out_3d.csv;
update temp_pyadmob_rev_1 set $8=0 where $8='None';
update temp_pyadmob_rev_1 set $7=0 where $7='None';
delete from ADMOB_PYTHON where RECORDDATE >= DATEADD(days,-3,CURRENT_DATE);
insert into ADMOB_PYTHON (select  * from temp_pyadmob_rev_1);
select recorddate,sum(earnings) from ADMOB_PYTHON where RECORDDATE >= DATEADD(days,-7,CURRENT_DATE)  group by recorddate order by recorddate desc;