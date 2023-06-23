package org.alex.db;

import org.alex.db.consts.Consts;
import org.alex.db.entity.ConnItem;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

/**
 * @author alex
 * @version 1.0.0
 * @since 2023-06-20 11:25
 */
public class Utils {

    // 根据连接名称获取连接配置对象
    public static ConnItem parseConfByFileName(String fileName) {
        ConnItem connItem = new ConnItem();
        ConnItem.ConnItemDetail connItemDetail = new ConnItem.ConnItemDetail();
        try {
            String confFileContent = Files.readString(Paths.get(Consts.CONF_PATH + fileName + ".conf"));
            String[] confFileContentArray = confFileContent.split(Consts.CONF_SPLIT);
            connItem.setConnName(confFileContentArray[0]);
            connItemDetail.setConnIp(confFileContentArray[1]);
            connItemDetail.setPort(Integer.valueOf(confFileContentArray[2]));
            connItemDetail.setUsername(confFileContentArray[3]);
            connItemDetail.setPassword(confFileContentArray[4]);

            connItem.setConnItemDetail(connItemDetail);

        } catch (IOException ioException) {

        }

        return connItem;
    }

    public static List<String> getConfNameList() {
        File file = new File(Consts.CONF_PATH);
        File[] fs = file.listFiles();
        if (fs == null ) {
            return Collections.emptyList();
        }

        return Arrays.stream(fs)
                .map(File::getName)
                .filter(item -> item.endsWith(".conf"))
                .collect(Collectors.toList());
    }
}
