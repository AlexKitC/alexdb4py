package org.alex.db.controller;

import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TreeItem;
import javafx.scene.control.TreeView;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.VBox;
import javafx.scene.text.Text;
import javafx.stage.Stage;
import org.alex.db.Bootstrap;
import org.alex.db.Utils;
import org.alex.db.db.DbConnUtils;
import org.alex.db.entity.ConnItem;

import java.io.IOException;
import java.net.URL;
import java.util.HashMap;
import java.util.List;
import java.util.Objects;
import java.util.ResourceBundle;

import static org.alex.db.consts.Consts.NEW_CONN_TITLE;

/**
 * @author alex
 * @version 1.0.0
 * @since 2023-06-20 10:15
 */
public class HomeController implements Initializable {

    @FXML
    private VBox leftVbox;
    @FXML
    private Button newConnButton;
    @FXML
    private Button newQueryButton;


    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        List<String> confNameList = Utils.getConfNameList();
        System.out.println(confNameList);

        if (confNameList.size() > 0) {
            HashMap<String, ConnItem> connItemHashMap = new HashMap<>();
            for (String item : confNameList) {
                connItemHashMap.put(item, Utils.parseConfByFileName(item));

                // 根据配置文件放入连接信息的tree rootItem
                TreeItem<String> rootItem = new TreeItem<>(item);

                TreeView<String> tree = new TreeView<>(rootItem);
                leftVbox.getChildren().add(tree);

                //如果双击treeView的Text名为配置文件名：说明是rootItem，执行sql获取表数据插入
                tree.addEventHandler(MouseEvent.MOUSE_CLICKED, mouseEvent -> {
                    String clickedConfName = mouseEvent.getTarget() instanceof Text ? ((Text) mouseEvent.getTarget()).getText() : "";
                    if (mouseEvent.getClickCount() == 2
                            && mouseEvent.getTarget() instanceof Text
                            && confNameList.contains(clickedConfName)) {
                        DbConnUtils.generateConn(connItemHashMap.get(clickedConfName));
                        List<String> databaseList = DbConnUtils.getDatabases();
                        addItemToTreeRootItemForDatabase(rootItem, databaseList, tree, connItemHashMap.get(clickedConfName));
                    }
                    System.out.println(mouseEvent.getTarget());
                });
            }
        }


    }

    private void addItemToTreeRootItemForDatabase(TreeItem<String> rootItem, List<String> databaseList, TreeView<String> tree, ConnItem connItem) {
        for (String db : databaseList) {
            TreeItem<String> item = new TreeItem<>(db);
            rootItem.getChildren().add(item);
            rootItem.setExpanded(true);
            tree.addEventHandler(MouseEvent.MOUSE_CLICKED, mouseEvent -> {
                String clickedDatabaseName = mouseEvent.getTarget() instanceof Text ? ((Text) mouseEvent.getTarget()).getText() : "";
                if (mouseEvent.getClickCount() == 2
                        && mouseEvent.getTarget() instanceof Text
                        && databaseList.contains(clickedDatabaseName)) {
                    DbConnUtils.generateConn(connItem);
                    List<String> tableList = DbConnUtils.getTables(clickedDatabaseName);
                    System.out.println(tableList);
                    addItemToTreeRootItemForTables(item, tableList, clickedDatabaseName);
                }
            });
        }

    }

    private void addItemToTreeRootItemForTables(TreeItem<String> databaseItem, List<String> tableList, String clickedDatabaseName) {
        if (databaseItem.getValue().equals(clickedDatabaseName)) {
            databaseItem.setExpanded(true);
            for (String table : tableList) {
                TreeItem<String> item = new TreeItem<>(table);
                databaseItem.getChildren().add(item);
            }
        }


    }


    @FXML
    private void onClickNewConnButton() throws IOException {
        Stage newConnStage = new Stage();
        Parent root = FXMLLoader.load(Objects.requireNonNull(getClass().getResource("/fxml/new-conn.fxml")));
        Scene scene = new Scene(root);
        newConnStage.setTitle(NEW_CONN_TITLE);
        newConnStage.setScene(scene);

        Bootstrap.connStage = newConnStage;
        newConnStage.show();
    }

    @FXML
    private void onClickNewQueryButton() {
        System.out.println("cli");
    }
}
