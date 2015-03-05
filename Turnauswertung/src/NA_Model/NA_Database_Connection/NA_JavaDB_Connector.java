package NA_Model.NA_Database_Connection;

import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.List;

public class NA_JavaDB_Connector extends NA_DB_Connector {

    public NA_JavaDB_Connector(String url){
        setDatabaseName(url);
    }

    protected void connect() {
        try {
            setConnection(DriverManager.getConnection(urlPrefix() + getDatabaseName() + urlSuffix()));
        } catch(SQLException e){
            e.printStackTrace();
        }
    }

    public void executeQuery(String query) {
        connect();
        try{
            Statement stmnt = getConnection().createStatement();
            stmnt.executeQuery(query);
        } catch (SQLException e){
            e.printStackTrace();
        }
        disconnect();
    }

    public List<String> retrieveData(String query) {
        connect();


        disconnect();
        return null;
    }

    // Constants
    protected String urlPrefix(){
        return super.urlPrefix()+"derby:";
    }

    protected String urlSuffix(){
        return ";create=true";
    }
}
