# -*- coding: utf-8 -*-  
# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.6 MB
# Time  Complexity: O(N)
# Space Complexity: O(N)
# solution 3, string
# https://leetcode.com/problems/tag-validator/discuss/279586/Python-One-pass-leveraging-State-Machine
'''
Here is a description of the state machine
state = [plain, open, close, cdata]
state-transfer-formula =
{
	plain: {
		'<![CDATA[': cdata, 
		'</': close
		'<': open
	}, 
	open: {
		'>': plain
	}, 
	close: {
		'>': plain
	}, 
	cdata: {
		']]>': plain
	}
}
'''
class Solution(object):
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        stack = []
        
        state = ["plain", "open", "close", "cdata"]
        curr = "plain"        
        
        open_tag = []
        close_tag = []
        
        idx = 0
        
        while idx < len(code):
            ch = code[idx]
                        
            if curr == "plain":
                if not stack and idx != 0:
                    # code is not in a closed tage
                    print('code is not in a closed tage')
                    return False
                
                if code[idx:idx+9] == "<![CDATA[":
                    curr = "cdata"
                    idx += 9
                    continue
                elif code[idx:idx+2] == '</':
                    curr = 'close'
                    idx += 2
                    continue
                elif ch == '<':
                    curr = "open"
                
            elif curr == "open":
                if ch == '>':
                    if len(open_tag) > 9 or len(open_tag) < 1:
                        print('open tag name length not valid')
                        return False
                    
                    stack.append("".join(open_tag))
                    open_tag = []
                    curr = 'plain'
                    idx += 1
                    continue
                
                if not ch.isupper():
                    print('open tag is not upper', ch)
                    return False
                
                open_tag.append(ch)
            
            elif curr == 'close':
                if ch == '>':
                    if len(close_tag) > 9 or len(close_tag) < 1:
                        print('close tag name length not valid')
                        return False
                    
                    close_tag_str = "".join(close_tag)
                    if not stack or close_tag_str != stack[-1]:
                        print('tag no match')
                        return False
                    else:
                        stack.pop()
                    
                    close_tag = []
                    curr = 'plain'
                    idx += 1
                    continue
                    
                if not ch.isupper():
                    print('close tag is not upper')
                    return False
                
                close_tag.append(ch)
                    
            elif curr == "cdata":
                if code[idx:idx+3] == ']]>':
                    idx += 3
                    curr = "plain"
                    continue
                    
            idx += 1
            
        print(curr)
                    
        if stack or curr != "plain":
            return False
        
        return True

def main():
    inputX,expectRes = "<DIV>This is the first line <![CDATA[<div>]]></DIV>",True
    obj = Solution()
    result = obj.isValid(inputX)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : "+ expectRes)
    
if __name__ =='__main__':
    main() 