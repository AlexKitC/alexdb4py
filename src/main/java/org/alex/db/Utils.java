package org.alex.db;

import org.alex.db.consts.Consts;
import org.alex.db.entity.ConnItem;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
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


        try (BufferedReader br = Files.newBufferedReader(Paths.get(Consts.CONF_PATH + fileName))) {
            String confFileContent;
            List<String> confFileContentArray = new ArrayList<>(8);
            while ((confFileContent = br.readLine()) != null) {
                confFileContentArray.add(confFileContent);
            }

            connItem.setConnName(confFileContentArray.get(0));
            connItemDetail.setConnIp(confFileContentArray.get(1));
            connItemDetail.setPort(Integer.valueOf(confFileContentArray.get(2)));
            connItemDetail.setUsername(confFileContentArray.get(3));
            connItemDetail.setPassword(confFileContentArray.get(4));

            connItem.setConnItemDetail(connItemDetail);
        } catch (IOException e) {
            throw new RuntimeException(e);
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
