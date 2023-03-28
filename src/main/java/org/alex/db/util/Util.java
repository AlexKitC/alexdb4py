package org.alex.db.util;

import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import org.alex.db.Db;
import org.alex.db.var.ConstVar;

import java.io.IOException;
import java.util.Objects;

/**
 * @author alex
 * @version 1.0.0
 * @since 2023/3/28 10:19
 */
public class Util {
    private volatile static Util instance;
    private Util (){}
    public static Util getInstance() {
        if (instance == null) {
            synchronized (Util.class) {
                if (instance == null) {
                    instance = new Util();
                }
            }
        }
        return instance;
    }

    public void loadScene(String fxmlName) {
        try {
            Parent root = FXMLLoader.load(Objects.requireNonNull(getClass().getResource(String.format("/fxml/%s.fxml", fxmlName))));
            Db.APP.setScene(new Scene(root));
            Db.APP.setTitle(ConstVar.TITLE);
            Db.APP.show();
        } catch (IOException e) {

        }
    }
}
