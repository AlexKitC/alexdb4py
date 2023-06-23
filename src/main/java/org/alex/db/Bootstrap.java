package org.alex.db;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.Objects;

/**
 * @author alex
 * @version 1.0.0
 * @since 2023-06-19 22:34
 */
public class Bootstrap extends Application {

    public static Stage homeStage;
    public static Stage connStage;
    @Override
    public void start(Stage stage) throws IOException {
        Parent root = FXMLLoader.load(Objects.requireNonNull(getClass().getResource("/fxml/home.fxml")));
        Scene scene = new Scene(root);
        stage.setScene(scene);
        stage.setTitle("AlexDB-by Alex-黑白");

        homeStage = stage;
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
