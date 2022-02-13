from impala.dbapi import connect
from krbcontext import krbcontext

keytab_path = 'krb/hive_user2.keytab'
principal = 'hive/user2@HADOOP.COM'
with krbcontext(
        using_keytab=True,
        principal=principal,
        keytab_file=keytab_path):

    # from java: jdbc:hive2://10.36.248.27:8719/default;principal=hive/quickstart.cloudera@HADOOP.COM
    conn = connect(
        host='10.36.248.27',
        port=8719,
        database='default',
        auth_mechanism='GSSAPI',
        kerberos_service_name='hive',
        krb_host='quickstart.cloudera')

    cursor = conn.cursor()
    cursor.execute('show tables')
    for row in cursor:
        print(row)
