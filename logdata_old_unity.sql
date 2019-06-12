put file://C:\Users\muthu_000\Python3.7\Unityanalytics\output_file_all.csv @my_int_Stage_csv;
create or replace table temp_pyunity_rev_1 as select  $1,$2,$3,$4,$5,$6,$7,$8,$9 from @my_int_stage_csv/output_file_all.csv;
alter table TEMP_PYUNITY_REV_1 add ECPM float;
update TEMP_PYUNITY_REV_1 set ecpm=($9/$8)*1000 where $9>0 and $8>0;
insert into UNITY_PYTHON (select  * from temp_pyUNITY_rev_1);
update unity_python set impressions_rpm=(earnings/impressions)*1000 where earnings>0 and impressions>0;
update UNITY_PYTHON set impressions_RPM=0 where impressions_RPM is Null;
alter table temp_pyunity_rev_1 drop ecpm;
select recorddate,sum(earnings) from UNITY_PYTHON   group by recorddate order by recorddate desc;