put file://C:\Users\muthu_000\Python3.7\work\output_file_1.csv @my_int_Stage_csv;
create or replace table temp_pyunity_rev_1 as select  $1,$2,$3,$4,$5,$6,$7,$8,$9 from @my_int_stage_csv/output_file_1.csv;
alter table TEMP_PYUNITY_REV_1 add ECPM float;
update TEMP_PYUNITY_REV_1 set ecpm=($9/$8)*1000 where $9>0;
delete from UNITY_PYTHON where RECORDDATE >= DATEADD(days,-4,CURRENT_DATE);
insert into UNITY_PYTHON (select  * from temp_pyUNITY_rev_1);
alter table temp_pyunity_rev_1 drop ecpm;
select recorddate,sum(earnings) from UNITY_PYTHON where RECORDDATE >= DATEADD(days,-7,CURRENT_DATE)  group by recorddate order by recorddate desc;
select recorddate,sum(earnings) from ADMOB_PYTHON where RECORDDATE >= DATEADD(days,-7,CURRENT_DATE)  group by recorddate order by recorddate desc;