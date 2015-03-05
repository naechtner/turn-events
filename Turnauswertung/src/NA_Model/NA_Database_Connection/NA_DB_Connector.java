package NA_Model.NA_Database_Connection;

import com.ibatis.common.jdbc.ScriptRunner;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.Reader;
import java.sql.Connection;
import java.sql.SQLException;
import java.util.List;

public abstract class NA_DB_Connector {
    private String databaseName;
    private Connection connection;

    protected Connection getConnection(){
        return connection;
    }

    protected void setConnection(Connection newConnection){
        connection = newConnection;
    }

    protected String getDatabaseName(){
        return databaseName;
    }

    protected void setDatabaseName(String newUrl){
        databaseName = newUrl;
    }

    protected abstract void connect();

    protected void disconnect(){
        try{
            getConnection().close();
        } catch (SQLException e){
            e.printStackTrace();
        }
    }

    public abstract void executeQuery(String query);

    public abstract List<String> retrieveData(String query);

    public void initializeScheme(){

//        try {
//            // Initialize object for ScripRunner
//            ScriptRunner sr = new ScriptRunner(getConnection(), false, false);
//
//            // Give the input file to Reader
//            Reader reader = new BufferedReader(new FileReader("src/NA_Model/NA_Database_Connection/DB_Scheme.sql"));
//            System.out.println(reader.read());
//
//            // Exctute script
//            sr.runScript(reader);
//
//        } catch (Exception e) {
//            e.printStackTrace();
//        }
    }

    // Constants
    protected String urlPrefix(){
        return "jdbc:";
    }
}