## specification

- codes are not available here because these codes are the owned by [Tianrang Inc.](https://www.tianrang.com/)

## input

```sql
SELECT DISTINCT
    new_dmp.rpt_mdmp_usershop_d.__aid AS __aid
FROM
    new_dmp.rpt_mdmp_usershop_d
WHERE (
    new_dmp.rpt_mdmp_usershop_d.tcif_is_cart_auction IN ('1') AND
    new_dmp.rpt_mdmp_usershop_d.shop_id IN ('65716507', '65716507') AND
    new_dmp.rpt_mdmp_usershop_d.tcif_pv_num_30d >= 1 AND
    new_dmp.rpt_mdmp_usershop_d.tcif_pv_num_30d <= 20 AND
    new_dmp.rpt_mdmp_usershop_d.shop_id IN ('65716507', '65716507') AND
    new_dmp.rpt_mdmp_usershop_d.tcif_alipay_num_180d >= 0 AND
    new_dmp.rpt_mdmp_usershop_d.tcif_alipay_num_180d <= 0 AND
    new_dmp.rpt_mdmp_usershop_d.shop_id IN ('65716507', '65716507')
)
```

## output

```json
[
    {"optionGroupId": 258, "operatorType": 1, "tagName": "购物车是否有店铺宝贝", "tagId": 110012, "type": "SHOP", "value": 12345},
    {"optionGroupId": 65, "operatorType": 1, "tagName": "购物车是否有店铺宝贝", "tagId": 110012, "type": "RADIO", "value": "1"},
    {"optionGroupId": 283, "operatorType": 1, "tagName": "最近180天店内总购买笔数", "tagId": 110039, "type": "SHOP", "value": 12345},
    {"optionGroupId": 90, "operatorType": 1, "tagName": "最近180天店内总购买笔数", "tagId": 110039, "type": "INPUT", "value": "0~0"},
    {"optionGroupId": 267, "operatorType": 1, "tagName": "最近30天店内宝贝页总浏览量", "tagId": 110021, "type": "SHOP", "value": 12345},
    {"optionGroupId": 74, "operatorType": 1, "tagName": "最近30天店内宝贝页总浏览量", "tagId": 110021, "type": "INPUT", "value": "1~20"}
]
```

