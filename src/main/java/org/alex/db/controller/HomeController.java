package org.alex.db.controller;

import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.TreeItem;
import javafx.scene.control.TreeView;
import org.alex.db.entity.ConnItem;

import java.net.URL;
import java.util.ResourceBundle;

/**
 * @author alex
 * @version 1.0.0
 * @since 2023-06-20 10:15
 */
public class HomeController implements Initializable {

    @FXML
    private TreeView<ConnItem> connItemTreeView;


    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        ConnItem item = new ConnItem()
                .setConnName("dev-yhc");
        TreeItem<ConnItem> rootItem = new TreeItem<>(item);
        rootItem.setExpanded(true);
        rootItem.getChildren().add(new TreeItem<>());
        connItemTreeView = new TreeView<>(rootItem);
    }
}
