package org.alex.db.controller;

import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.CheckBox;
import javafx.scene.control.TextField;
import org.alex.db.Bootstrap;
import org.alex.db.consts.Consts;
import org.alex.db.entity.ConnItem;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

/**
 * @author alex
 * @version 1.0.0
 * @since 2023/6/22 21:34
 */
public class NewConnController {



    @FXML
    private Button newConnTestConnButton;
    @FXML
    private Button newConnCancelButton;
    @FXML
    private Button newConnSaveButton;
    @FXML
    private TextField newConnNameTextField;
    @FXML
    private TextField newConnHostTextField;
    @FXML
    private TextField newConnPortTextField;
    @FXML
    private TextField newConnUsernameTextField;
    @FXML
    private TextField newConnPasswordTextField;
    @FXML
    private CheckBox newConnRememberPasswordCheckbox;

    // 测试连接
    @FXML
    private void onClickTestNewConn() {

    }

    //返回主页
    @FXML
    private void onClickCancelNewConn() {
        Bootstrap.connStage.close();
    }

    //存储连接
    @FXML
    private void onClickSaveNewConn() {
        //1.优先获取所有填写的连接信息
        ConnItem connItem = getConnItem();
        //2.存储当前连接信息到file
        storeConnItem(connItem);
        //3.关闭当前连接stage
        Bootstrap.connStage.close();
        //4.插入连接-tree
    }

    private void storeConnItem(ConnItem connItem) {
        String filePath = String.format("%s/%s.conf", Consts.CONF_PATH, connItem.getConnName());
        StringBuilder fileContent = new StringBuilder();
        fileContent.append(connItem.getConnName())
                .append(Consts.CONF_SPLIT)
                .append(connItem.getConnItemDetail().getConnIp())
                .append(Consts.CONF_SPLIT)
                .append(connItem.getConnItemDetail().getPort())
                .append(Consts.CONF_SPLIT)
                .append(connItem.getConnItemDetail().getUsername())
                .append(Consts.CONF_SPLIT)
                .append(connItem.getConnItemDetail().getPassword());

        FileOutputStream fileOutputStream = null;
        File file;

        try {
            file = new File(filePath);
            fileOutputStream = new FileOutputStream(file);

            //文件不存在则新建
            if (!file.exists()) {
                file.createNewFile();
            }

            byte[] contentBytes = fileContent.toString().getBytes();
            fileOutputStream.write(contentBytes);
            fileOutputStream.flush();
            fileOutputStream.close();
        } catch (IOException ioException) {

        }

    }

    private ConnItem getConnItem() {
        var connItem = new ConnItem();
        var connName = newConnNameTextField.getText();

        connItem.setConnName(connName);
        var connItemDetail = new ConnItem.ConnItemDetail();
        var connAddress = newConnHostTextField.getText();
        var connPort = newConnPortTextField.getText();
        var connUsername = newConnUsernameTextField.getText();
        var connPassword = newConnPasswordTextField.getText();

        connItemDetail.setConnIp(connAddress)
                .setPort(connPort.isEmpty() ? 0 : Integer.parseInt(connPort))
                .setUsername(connUsername)
                .setPassword(connPassword);
        connItem.setConnItemDetail(connItemDetail);

        validConnItem(connItem);

        return connItem;
    }

    // 校验填写的连接信息
    private void validConnItem(ConnItem connItem) {
        if (connItem.getConnName().isEmpty()) {
            newConnNameTextField.setText("连接名称未填写！请填写");
            newConnNameTextField.requestFocus();
        } else if (connItem.getConnItemDetail().getConnIp().isEmpty()) {
            newConnHostTextField.setText("连接地址未填写！请填写");
            newConnHostTextField.requestFocus();
        } else if (connItem.getConnItemDetail().getPort() == 0) {
            newConnPortTextField.setText("端口未填写！请填写");
            newConnPortTextField.requestFocus();
        } else if (connItem.getConnItemDetail().getUsername().isEmpty()) {
            newConnUsernameTextField.setText("用户名未填写！请填写");
            newConnUsernameTextField.requestFocus();
        } else if (connItem.getConnItemDetail().getPassword().isEmpty()) {
            newConnPasswordTextField.setText("密码未填写！请填写");
            newConnPasswordTextField.requestFocus();
        }
    }
}
