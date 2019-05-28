### display.py
1. 配置是否显示bounding box，mask以及labal
2. 修改涂色的深度
3. 修改保存图片的地址
```python
plt.savefig('/home/zbf/zhaozhao/data/6/rgb_mask_box_5/{}'.format(name))
```
### test.py
1. 利用COCO数据集进行语义分割
修改图片的地址
```python
MY_IMAGE_DIR = os.path.abspath('/home/zbf/zhaozhao/data/6/rgb/')
```