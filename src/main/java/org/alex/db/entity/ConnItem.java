package org.alex.db.entity;

import lombok.Data;
import lombok.experimental.Accessors;

/**
 * @author alex
 * @version 1.0.0
 * @since 2023-06-20 11:36
 */
@Data
@Accessors(chain = true)
public class ConnItem {

    private String connName;

    private Boolean isActived;

    private ConnItemDetail connItemDetail;

    @Data
    @Accessors(chain = true)
    public static class ConnItemDetail {
        private String connIp;

        private Integer port;

        private String username;

        private String password;
    }

    @Override
    public String toString() {
        return connName;
    }
}
