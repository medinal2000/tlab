# Code from https://github.com/warmspringwinds/pytorch-segmentation-detection/blob/master/pytorch_segmentation_detection/utils/flops_benchmark.py


import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class FlopsCounter:
    def __init__(self, main):
        self._count = None
        self._main = main
        for m in main.modules():
            m.register_forward_hook(self._add_flops)


    def count(self, input):
        self._count = 0
        self._main(input)
        c = self._count
        self._count = None
        return c


    def _add_flops(self, module, input=[0], output=[0]):
        my_flop_count_based_on_input = 0

        if self._count is not None:
            if isinstance(module, nn.Conv2d):
                output_height, output_width = output.shape[2:]
                kernel_height, kernel_width = module.kernel_size
                in_channels = module.in_channels
                out_channels = module.out_channels

                # We count multiply-add as 2 flops
                conv_per_position_flops = 2 * kernel_height * kernel_width * in_channels * out_channels
                active_elements_count = output_height * output_width
                my_flop_count_based_on_input += conv_per_position_flops * active_elements_count

                if module.bias is not None:
                    my_flop_count_based_on_input += out_channels * active_elements_count

            elif isinstance(module, nn.Linear):
                my_flop_count_based_on_input += module.in_features
                if module.bias is not None:
                    my_flop_count_based_on_input += module.out_features

            elif isinstance(module, nn.ReLU):
                input = input[0]
                my_flop_count_based_on_input += input.shape[0] * input.shape[1] * input.shape[2] * input.shape[3]

            elif isinstance(module, nn.Sequential):
                pass

            elif isinstance(module, nn.MaxPool2d):
                #https://machinethink.net/blog/how-fast-is-my-model/
                #this will be inaccurate if stride != kernel
                input = input[0]
                my_flop_count_based_on_input += input.shape[0] * input.shape[1] * input.shape[2]

            elif isinstance(module, nn.modules.pooling.AvgPool2d):
                input = input[0]
                my_flop_count_based_on_input += input.shape[0] * input.shape[1] * input.shape[2]
                my_flop_count_based_on_input += math.floor(module.stride/input.shape[0]) * (module.stride/input.shape[1]) * input.shape[2]


            elif isinstance(module, nn.modules.batchnorm.BatchNorm2d):
                input = input[0]
                my_flop_count_based_on_input += 6 * input.shape[0] * input.shape[1] * input.shape[2] * input.shape[3]

            #would have to implement _get_flops as an attribute for each module
            elif hasattr(module, "_get_flops"):
                my_flop_count_based_on_input += module._get_flops(input)

            else:
                print(f"* Unknown {module.__class__}")

            self._count += my_flop_count_based_on_input
        return


## USAGE
## n = Net()
## fc = FlopsCounter(n)
## flops = (fc.count(Net_Input)))
