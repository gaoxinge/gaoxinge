import cv2
import numpy as np
import tensorflow as tf

origin_color = (125, 125, 125)
light_color = (1, 1, 1)
k_a = 0.1
k_d = 1
k_s = 0.5
p = 32

img = np.zeros((500, 500, 3), dtype=np.uint8)
for x in range(500):
    for y in range(500):
        if (250 - x) ** 2 + (250 - y) ** 2 <= 200 ** 2:
            img[y, x, 0] = origin_color[0]
            img[y, x, 1] = origin_color[1]
            img[y, x, 2] = origin_color[2]

x = tf.reshape(tf.tile(tf.range(0, 500, dtype=tf.float64), [500]), (500, 500))
y = tf.transpose(x)
m = (250 - x) ** 2 + (250 - y) ** 2 <= 200 ** 2
x = tf.where(m, x, 0)
y = tf.where(m, y, 0)
z = tf.where(m, tf.sqrt(200 ** 2 - (250 - x) ** 2 - (250 - y) ** 2), 0)
xyz = tf.stack((x, y, z), axis=2)
norm_vector = xyz - (250, 250, 0)
norm_vector /= tf.reshape(tf.sqrt(tf.reduce_sum(norm_vector ** 2, axis=2)), (500, 500, 1))
view_vector = (0, 0, 1) - tf.zeros((500, 500, 3), dtype=tf.float64)
light_vector = (-np.sqrt(3) / 3, -np.sqrt(3) / 3, np.sqrt(3) / 3) - tf.zeros((500, 500, 3), dtype=tf.float64)
half_vector = view_vector + light_vector
half_vector /= tf.reshape(tf.sqrt(tf.reduce_sum(half_vector ** 2, axis=2)), (500, 500, 1))
cos_d = tf.maximum(0, tf.reduce_sum(norm_vector * light_vector, axis=2))
cos_s = tf.maximum(0, tf.pow(tf.maximum(0, tf.reduce_sum(norm_vector * half_vector, axis=2)), p))
alpha = k_a + k_d * cos_d + k_s * cos_s
img2 = tf.minimum(255, tf.reshape(alpha, (500, 500, 1)) * (light_color * tf.convert_to_tensor(img, dtype=tf.float64)))
img2 = img2.numpy()
img2 = img2.astype(np.uint8)

cv2.imshow("fuck", img2)
cv2.waitKey()
