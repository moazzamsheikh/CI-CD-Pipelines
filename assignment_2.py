import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class LoginTest {

    private final Login login = new Login();

    @Test
    public void testInValidLogin() {
        assertFalse(login.validate("umairlatif@example.com", "password456"), "InValid login should return false.");

    }

    @Test
    public void testInvalidEmail() {
        assertFalse(login.validate("invalid@example.com", "password123"), "Invalid email should return false.");
    }

    @Test
    public void testIncorrectPassword() {
        assertFalse(login.validate("johndoe@example.com", "wrong password"), "Incorrect password should return false.");
    }

    @Test
    public void testEmptyFields() {
        assertFalse(login.validate("", ""), "Empty fields should return false.");
    }

    @Test
    public void testSQLInjection() {
        assertFalse(login.validate("' OR 1=1 --", "password123"), "SQL injection attempt should return false.");
    }

}
