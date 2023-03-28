package org.alex.db;

import javafx.application.Application;
import javafx.stage.Stage;
import org.alex.db.util.Util;

/**
 * @author alex
 * @version 1.0.0
 * @since 2022-03-28 10:00:07
 */
public class Db extends Application {
    public static Stage APP;

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage stage) {
        APP = stage;
        Util.getInstance().loadScene("home");
    }
}