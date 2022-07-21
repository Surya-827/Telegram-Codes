class Solution {
    private int ans=0;
    public int pathSum(TreeNode root, int targetSum) {
        if(root == null) return 0;
        helper(root, targetSum, 0);
        pathSum(root.left, targetSum);
        pathSum(root.right, targetSum);
        return ans;
    }
    public void helper(TreeNode root, int targetSum , long pathSum){
        if(root == null) return;
        pathSum += root.val;
        if(pathSum == targetSum ){
            ans++;
        }
        helper(root.left,targetSum, pathSum);
        helper(root.right,targetSum, pathSum);
    }
}
