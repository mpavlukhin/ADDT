from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from django.conf import settings

import time

import numpy as np
import tensorflow as tf


class ConvolutionalNeuralNetworkAnalyzer:
    animals = None

    def __init__(self):
        self.animals = settings.ANIMALS

    def load_graph(self, model_file):
        graph = tf.Graph()
        graph_def = tf.GraphDef()

        with open(model_file, "rb") as f:
            graph_def.ParseFromString(f.read())
        with graph.as_default():
            tf.import_graph_def(graph_def)

        return graph

    def read_tensor_from_image_file(self, file_name, input_height=299, input_width=299,
                                    input_mean=0, input_std=255):
        input_name = "file_reader"
        output_name = "normalized"
        file_reader = tf.read_file(file_name, input_name)
        if file_name.endswith(".png"):
            image_reader = tf.image.decode_png(file_reader, channels=3,
                                               name='png_reader')
        elif file_name.endswith(".gif"):
            image_reader = tf.squeeze(tf.image.decode_gif(file_reader,
                                                          name='gif_reader'))
        elif file_name.endswith(".bmp"):
            image_reader = tf.image.decode_bmp(file_reader, name='bmp_reader')
        else:
            image_reader = tf.image.decode_jpeg(file_reader, channels=3,
                                                name='jpeg_reader')
        float_caster = tf.cast(image_reader, tf.float32)
        dims_expander = tf.expand_dims(float_caster, 0);
        resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
        normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
        sess = tf.Session()
        result = sess.run(normalized)

        return result

    def load_labels(self, label_file):
        label = []
        proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
        for l in proto_as_ascii_lines:
            label.append(l.rstrip())
        return label

    def label_image(self, file_name, model_file="neural/cnn/tf_files/retrained_graph.pb",
                    label_file = "neural/cnn/tf_files/retrained_labels.txt"):
        input_height = 224
        input_width = 224
        input_mean = 128
        input_std = 128
        input_layer = "input"
        output_layer = "final_result"

        graph = self.load_graph(model_file)
        t = self.read_tensor_from_image_file(file_name,
                                        input_height=input_height,
                                        input_width=input_width,
                                        input_mean=input_mean,
                                        input_std=input_std)

        input_name = "import/" + input_layer
        output_name = "import/" + output_layer
        input_operation = graph.get_operation_by_name(input_name);
        output_operation = graph.get_operation_by_name(output_name);

        with tf.Session(graph=graph) as sess:
            start = time.time()
            results = sess.run(output_operation.outputs[0],
                               {input_operation.outputs[0]: t})
            end = time.time()
        results = np.squeeze(results)

        top_k = results.argsort()[-5:][::-1]
        labels = self.load_labels(label_file)

        evaluation_time = '\nEvaluation time (1-image): {:.3f}s\n'.format(end - start)

        conclusion = evaluation_time

        template = "{} (score={:0.5f})"
        for i in top_k:
            conclusion += template.format(labels[i], results[i]) + '\n'
        is_sick = False

        if labels[0].find('sick') > -1:
            is_sick = True

        return is_sick, conclusion

    def process_biochemical_analysis_data(self, data_dict, image):
        animal = data_dict['animal']

        is_sick, conclusion = self.label_image(image)

        return is_sick, conclusion