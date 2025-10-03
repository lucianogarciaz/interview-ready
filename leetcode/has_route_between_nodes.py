from collections import deque
from typing import List, Optional
import unittest


class GraphNode:
    def __init__(self, val: int = 0, neighbors: Optional[List['GraphNode']] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def hasRouteBetweenNodes(self, start: GraphNode, end: GraphNode) -> bool:
        visited: List[GraphNode] = []
        return self.dfs(start, end, visited)
    
    def dfs(self, start: GraphNode, end: GraphNode, visited: List[GraphNode]) -> bool:
        if start == end:
            return True
        if start in visited:
            return False
        
        visited.append(start)
        
        for neighbor in start.neighbors:
            if self.dfs(neighbor, end, visited):
                return True

        return False


class TestHasRouteBetweenNodes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        
        # Create test graph:
        # 1 -> 2 -> 3
        #  \    \    \
        #   v    v    v
        #   4 -> 5 -> 6
        #        ^
        #        |
        #        7
        
        self.node1 = GraphNode(1)
        self.node2 = GraphNode(2)
        self.node3 = GraphNode(3)
        self.node4 = GraphNode(4)
        self.node5 = GraphNode(5)
        self.node6 = GraphNode(6)
        self.node7 = GraphNode(7)
        
        # Set up connections
        self.node1.neighbors = [self.node2, self.node4]
        self.node2.neighbors = [self.node3, self.node5]
        self.node3.neighbors = [self.node6]
        self.node4.neighbors = [self.node5]
        self.node5.neighbors = [self.node6]
        self.node7.neighbors = [self.node5]
        
        # Create isolated node
        self.isolated_node = GraphNode(99)

    def test_direct_connection(self):
        """Test nodes that are directly connected"""
        self.assertTrue(self.solution.hasRouteBetweenNodes(self.node1, self.node2))
        self.assertTrue(self.solution.hasRouteBetweenNodes(self.node2, self.node3))
        self.assertTrue(self.solution.hasRouteBetweenNodes(self.node4, self.node5))

    def test_indirect_connection(self):
        """Test nodes that are connected through multiple hops"""
        self.assertTrue(self.solution.hasRouteBetweenNodes(self.node1, self.node6))
        self.assertTrue(self.solution.hasRouteBetweenNodes(self.node1, self.node5))
        self.assertTrue(self.solution.hasRouteBetweenNodes(self.node7, self.node6))

    def test_same_node(self):
        """Test when start and end are the same node"""
        self.assertTrue(self.solution.hasRouteBetweenNodes(self.node1, self.node1))
        self.assertTrue(self.solution.hasRouteBetweenNodes(self.node5, self.node5))

    def test_no_connection(self):
        """Test nodes that are not connected"""
        self.assertFalse(self.solution.hasRouteBetweenNodes(self.node6, self.node1))
        self.assertFalse(self.solution.hasRouteBetweenNodes(self.node3, self.node7))
        self.assertFalse(self.solution.hasRouteBetweenNodes(self.node1, self.node7))

    def test_isolated_node(self):
        """Test with isolated node (no neighbors)"""
        self.assertTrue(self.solution.hasRouteBetweenNodes(self.isolated_node, self.isolated_node))
        self.assertFalse(self.solution.hasRouteBetweenNodes(self.node1, self.isolated_node))
        self.assertFalse(self.solution.hasRouteBetweenNodes(self.isolated_node, self.node1))

    def test_cycle_detection(self):
        """Test that cycles don't cause infinite loops"""
        # Create a cycle: A -> B -> C -> A
        node_a = GraphNode('A')
        node_b = GraphNode('B')
        node_c = GraphNode('C')
        
        node_a.neighbors = [node_b]
        node_b.neighbors = [node_c]
        node_c.neighbors = [node_a]
        
        # Should be able to find route within cycle
        self.assertTrue(self.solution.hasRouteBetweenNodes(node_a, node_c))
        self.assertTrue(self.solution.hasRouteBetweenNodes(node_b, node_a))
        
        # But not to external nodes
        self.assertFalse(self.solution.hasRouteBetweenNodes(node_a, self.node1))

    def test_bidirectional_cycle(self):
        """Test bidirectional connections in a cycle"""
        # Create bidirectional cycle: A <-> B <-> C <-> A
        node_a = GraphNode('A')
        node_b = GraphNode('B')
        node_c = GraphNode('C')
        
        node_a.neighbors = [node_b, node_c]
        node_b.neighbors = [node_a, node_c]
        node_c.neighbors = [node_a, node_b]
        
        # All nodes should be reachable from any other node
        self.assertTrue(self.solution.hasRouteBetweenNodes(node_a, node_b))
        self.assertTrue(self.solution.hasRouteBetweenNodes(node_a, node_c))
        self.assertTrue(self.solution.hasRouteBetweenNodes(node_b, node_a))
        self.assertTrue(self.solution.hasRouteBetweenNodes(node_b, node_c))
        self.assertTrue(self.solution.hasRouteBetweenNodes(node_c, node_a))
        self.assertTrue(self.solution.hasRouteBetweenNodes(node_c, node_b))

    def test_empty_neighbors(self):
        """Test nodes with empty neighbors list"""
        empty_node1 = GraphNode(100, [])
        empty_node2 = GraphNode(101, [])
        
        self.assertTrue(self.solution.hasRouteBetweenNodes(empty_node1, empty_node1))
        self.assertFalse(self.solution.hasRouteBetweenNodes(empty_node1, empty_node2))
        self.assertFalse(self.solution.hasRouteBetweenNodes(empty_node1, self.node1))

    def test_complex_graph(self):
        """Test a more complex graph structure"""
        # Create a complex graph:
        #     A
        #    / \
        #   B   C
        #  / \ / \
        # D   E   F
        #  \ / \ /
        #   G   H
        
        node_a = GraphNode('A')
        node_b = GraphNode('B')
        node_c = GraphNode('C')
        node_d = GraphNode('D')
        node_e = GraphNode('E')
        node_f = GraphNode('F')
        node_g = GraphNode('G')
        node_h = GraphNode('H')
        
        node_a.neighbors = [node_b, node_c]
        node_b.neighbors = [node_d, node_e]
        node_c.neighbors = [node_e, node_f]
        node_d.neighbors = [node_g]
        node_e.neighbors = [node_g, node_h]
        node_f.neighbors = [node_h]
        
        # Test various connections
        self.assertTrue(self.solution.hasRouteBetweenNodes(node_a, node_g))  # A->B->D->G
        self.assertTrue(self.solution.hasRouteBetweenNodes(node_a, node_h))  # A->C->E->H or A->C->F->H
        self.assertTrue(self.solution.hasRouteBetweenNodes(node_b, node_g))  # B->D->G
        self.assertTrue(self.solution.hasRouteBetweenNodes(node_b, node_h))  # B->E->H
        
        # Test unreachable paths
        self.assertFalse(self.solution.hasRouteBetweenNodes(node_g, node_a))  # No path back to A
        self.assertFalse(self.solution.hasRouteBetweenNodes(node_h, node_d))  # No path from H to D
        self.assertFalse(self.solution.hasRouteBetweenNodes(node_b, node_f))  # No path from B to F

    def test_self_loop(self):
        """Test node with self-loop"""
        self_loop_node = GraphNode('self_loop')
        self_loop_node.neighbors = [self_loop_node]
        
        self.assertTrue(self.solution.hasRouteBetweenNodes(self_loop_node, self_loop_node))
        self.assertFalse(self.solution.hasRouteBetweenNodes(self_loop_node, self.node1))

    def test_visited_tracking(self):
        """Test that visited nodes are properly tracked to avoid infinite loops"""
        # Create a graph where we need to track visited nodes
        # A -> B -> C -> B (cycle back to B)
        node_a = GraphNode('A')
        node_b = GraphNode('B')
        node_c = GraphNode('C')
        
        node_a.neighbors = [node_b]
        node_b.neighbors = [node_c]
        node_c.neighbors = [node_b]  # Creates cycle
        
        # Should handle cycle correctly
        self.assertTrue(self.solution.hasRouteBetweenNodes(node_a, node_c))
        self.assertFalse(self.solution.hasRouteBetweenNodes(node_a, self.node1))


if __name__ == '__main__':
    unittest.main()