package org.alex.db.controller;

import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TreeItem;
import javafx.scene.control.TreeView;
import javafx.stage.Stage;
import org.alex.db.Bootstrap;
import org.alex.db.Utils;
import org.alex.db.entity.ConnItem;

import java.io.IOException;
import java.net.URL;
import java.util.List;
import java.util.Objects;
import java.util.ResourceBundle;

/**
 * @author alex
 * @version 1.0.0
 * @since 2023-06-20 10:15
 */
public class HomeController implements Initializable {

    @FXML
    private TreeView<ConnItem> connItemTreeView;
    @FXML
    private Button newConnButton;
    @FXML
    private Button newQueryButton;


    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        List<String> confNameList = Utils.getConfNameList();
        System.out.println(confNameList);
    }


    @FXML
    private void onClickNewConnButton() throws IOException {
        Stage newConnStage = new Stage();
        Parent root = FXMLLoader.load(Objects.requireNonNull(getClass().getResource("/fxml/new-conn.fxml")));
        Scene scene = new Scene(root);
        newConnStage.setTitle("新建连接");
        newConnStage.setScene(scene);

        Bootstrap.connStage = newConnStage;
        newConnStage.show();
    }

    @FXML
    private void onClickNewQueryButton() {
        System.out.println("cli");
    }
}
