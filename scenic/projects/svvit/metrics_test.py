"""Unit tests for functions in metrics.py."""

from absl.testing import parameterized
import jax.numpy as jnp
from scenic.projects.svvit import metrics


class MetricsTest(parameterized.TestCase):

  def setUp(self):
    self.one_hot_targets = jnp.array([[1, 0, 0], [0, 0, 1], [0, 1, 0],
                                      [0, 1, 0]])
    self.logits = jnp.array([[0.41, 0.39, 0.2], [0.4, 0.6, 0], [0.5, 0.1, 0.4],
                             [0.3, 0.5, 0.2]])
    super().setUp()

  def test_truvari_presicion(self):
    precision = metrics.truvari_precision(self.logits, self.one_hot_targets)
    self.assertEqual(0.5, precision)

  def test_truvari_recall(self):
    recall = metrics.truvari_recall(self.logits, self.one_hot_targets)
    self.assertEqual(1 / 3, recall)

  def test_truvari_presicion_events(self):
    precision_events = metrics.truvari_precision_events(self.logits,
                                                        self.one_hot_targets)
    self.assertEqual(1, precision_events)

  def test_truvari_recall_events(self):
    recall_events = metrics.truvari_recall_events(self.logits,
                                                  self.one_hot_targets)

    self.assertEqual(2 / 3, recall_events)
