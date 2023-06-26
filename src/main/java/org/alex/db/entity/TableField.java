package org.alex.db.entity;

import lombok.Data;
import lombok.experimental.Accessors;

/**
 * @author alex
 * @version 1.0.0
 * @since 2023-06-26 21:04
 */
@Data
@Accessors(chain = true)
public class TableField {

    private String columnName;

    private String remarks;

    private String typeName;

}
