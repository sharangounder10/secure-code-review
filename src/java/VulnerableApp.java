import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class VulnerableApp {

    // 1. Hardcoded credentials (Security Hotspot)
    private static final String PASSWORD = "password123";

    public void getUser(String userId) throws Exception {

        // 2. SQL Injection (Critical Vulnerability)
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost/db", "root", PASSWORD);
        Statement stmt = conn.createStatement();
        stmt.execute("SELECT * FROM users WHERE id = " + userId);
    }

    public void divide(int a, int b) {
        // 3. Possible division by zero (Bug)
        int result = a / b;
        System.out.println(result);
    }

    public void emptyCatch() {
        try {
            int x = 10 / 0;
        } catch (Exception e) {
            // 4. Empty catch block (Code Smell)
        }
    }
}