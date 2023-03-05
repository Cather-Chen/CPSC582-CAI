"""
Modified based on torch_geometric.nn.models.GNNExplainer
which generates explainations in node prediction tasks.

Citation:
Ying et al. GNNExplainer: Generating Explanations for Graph Neural Networks.
"""

from math import sqrt
import torch
from torch_geometric.nn import MessagePassing
import torch.nn.functional as F


