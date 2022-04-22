def users_tb():
    import mysql.connector as sql

    fit=sql.connect(host='localhost',user='root',passwd='rootABC',database='IPProject', port="3307")
    if fit.is_connected():
        print('Connected')
        c1 = fit.cursor()
        c1.execute(
            'create table users_tb(id int(10) AUTO_INCREMENT ,name varchar(65),email varchar(65),pwd varchar(65),fees int(65), primary key(id))')
        fit.commit()
        print('Table created !')


users_tb()
