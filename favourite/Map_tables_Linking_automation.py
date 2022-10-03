import psycopg2
import pandas as pd
from flask import Flask,render_template
import psycopg2
import pandas as pd
app=Flask(_name_)
con=psycopg2.connect(host='###########',dbname='###########',user='###########',password='###########',port=##########)
query1="""select * from common.rules_desc rd
join common.sample_master sm
on rd.id =rm.id
where mr.status='ACTIVE'
and rm.version =(select max(version) from common.sample_master sm2 where rd.id=sm2.id)
and rd.version= (select max(version) from common.rules_desc rd2 where rd.id2 =rd2.id2  and rd.id =rd2.id)
and mr.action =(select max(action) from common.rules_desc rd2 where rd.id2 =mr2.id2  and rd.id =rd2.id and rd.version=mr2.version );"""
table1=pd.read_sql(query1,con)
table1=table1.loc[:,~table1.columns.duplicated()]
con2=psycopg2.connect(host='###########',dbname='###########',user='###########',password='############',port=###########)
table2 =pd.read_sql(query1,con2)
table2=sit_table.loc[:,~table2.columns.duplicated()]
merge_df1=pd.merge(sit_table,dev_table,on=['id','id2'],how='inner',suffixes=('_table1','_table2'))
incorrect_ruleid=merge_df1[(merge_df1['sect_1']!=merge_df1['sect_2']) | (merge_df1['col_1']!=merge_df1['col_2']) | (merge_df1['item1']!=merge_df1['item2']) |(merge_df1['itemd1']!=merge_df1['itemd2']) ]
table_data=incorrect_ruleid[['id','id2','sect_1','sect_2','col_1','col_2','item1','item2','itemd1','itemd2']]
# To Export the data
# final=table_data.to_csv('Incorrect_column.csv')
# final
@app.route('/')
def table1():
    return table_data.to_html()
if _name=='main_':
    app.run()
