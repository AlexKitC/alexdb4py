package org.alex.db.db;

import org.alex.db.entity.ConnItem;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

/**
 * @author alex
 * @version 1.0.0
 * @since 2023-06-23 11:13
 */
public class DbConnUtils {

    private static Connection connection;
    private static Statement statement;

    public static void generateConn(ConnItem connItem) {
        try {
            Class.forName("com.mysql.jdbc.Driver");
        } catch (ClassNotFoundException classNotFoundException) {
            classNotFoundException.printStackTrace();
        }

        String url = String.format("jdbc:mysql://%s:%s",
                connItem.getConnItemDetail().getConnIp(),
                connItem.getConnItemDetail().getPort());
        try {
            connection = DriverManager.getConnection(url,
                    connItem.getConnItemDetail().getUsername(),
                    connItem.getConnItemDetail().getPassword());
            statement = connection.createStatement();

        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }
    }

    public static void doQuery(String sqlStatementString) {
        try {
            ResultSet resultSet = statement.executeQuery(sqlStatementString);
            while (resultSet.next()) {
//                System.out.println(resultSet.);
            }
            statement.close();
            connection.close();
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }

    }

    //获取当前连接下的所有数据库名称
    public static List<String> getDatabases() {
        List<String> dbNameList = new ArrayList<>();
        try {
            DatabaseMetaData databaseMetaData = connection.getMetaData();
            ResultSet resultSet = databaseMetaData.getCatalogs();
            while (resultSet.next()) {
                String dbName = resultSet.getString("TABLE_CAT");
                dbNameList.add(dbName);
            }
            statement.close();
            connection.close();
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }

        return dbNameList;
    }
}
