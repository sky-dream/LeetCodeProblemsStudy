import java.util.PriorityQueue;
class KthLargest {
    final PriorityQueue<Integer> q ;
    final int k;
    public KthLargest(int k, int[] nums) {
        this.k = k;
        q = new PriorityQueue<Integer>(k);
        for(int i: nums) {
            add(i);
        }
    }
    
    public int add(int val) {
        if(q.size() < k) {
            q.offer(val);
            
        }
        else if(q.peek() < val) {
            q.poll();
            q.offer(val);
        }
        return q.peek();
    }
}
public class kth_largest_element_in_a_stream{
    public static void main(String args[]){
        int k = 3;
        int nums[] = {4,5,8,2};
        KthLargest obj = new KthLargest(k, nums);
        int param_1 = obj.add(3);
        param_1 = obj.add(5);
        param_1 = obj.add(10);
        param_1 = obj.add(9);
        System.out.println("In java code,last return value is :" + param_1);
    }
}
/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */