class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        
        for ast in asteroids:
            while stack and ast < 0 < stack[-1]:
                #if left one is samll it destroyed
                if stack[-1] < -ast:
                    stack.pop()
                    continue
                #if both are same both destroyed
                elif stack[-1] == -ast:
                    stack.pop()
                break
                #if there is no let and still right exist then append
            else:
                stack.append(ast)
                
        return stack
