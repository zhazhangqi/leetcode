
import java.util.*;
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Leetcode623 {

    public TreeNode addOneRow(TreeNode root, int v, int d) {

        TreeNode temp = new TreeNode(v);
        if (d == 1){
            temp.left = root;
            temp.right = null;
            root = temp;
        }
        else{
            int CurrentDepth = 1;
            Queue<TreeNode> FatherNode = new LinkedList();
            Queue<TreeNode> ChildNode = new LinkedList();
            FatherNode.add(root);
            
            //Find the exact depth of the tree need to be added Value
            while (CurrentDepth != (d-1)){
                CurrentDepth = CurrentDepth + 1;
            
                while (!FatherNode.isEmpty()){
                    temp = FatherNode.poll();
                    if (temp.left!=null) ChildNode.add(temp.left);
                    if (temp.right!=null) ChildNode.add(temp.right);
                }
                FatherNode = ChildNode;
                Queue<TreeNode> EmptyNode = new LinkedList();
                ChildNode = EmptyNode;
            }

            while (!FatherNode.isEmpty()){
                temp = FatherNode.poll();
                
                TreeNode addNodeleft = new TreeNode(v);
                addNodeleft.left = temp.left;
                temp.left = addNodeleft;
                 
                TreeNode addNoderight = new TreeNode(v);
                addNoderight.right = temp.right;
                temp.right = addNoderight;
                
            }
        }
        return root;
    }

    public static void main(String[] args) {
        TreeNode rot = new TreeNode(1);
        rot.left = new TreeNode(2);
        rot.left.left = new TreeNode(4);
        rot.left.right = new TreeNode(5);       
        rot.right = new TreeNode(3);        
        rot.right.left = new TreeNode(6);
        Leetcode623 test = new Leetcode623();        
        TreeNode root = test.addOneRow(rot,10,4);
        
    }
}