def solutions(ranks):
    """
    public int solution(String S) {
        char[] arr = S.toCharArray();
	    List<Character> characterList = new ArrayList<Character>();
	    String b = "BALLOON";

	    for (char c:arr) {
	        characterList.add(c);
	    }
	    char[] ballonCharacterList = b.toCharArray();
	    boolean isChecked = true;
	    int count = 0;

	    while(isChecked) {
	        for (int i = 0; i < ballonCharacterList.length; i++) {
	            if(characterList.contains(ballonCharacterList[i])) {
	                characterList.remove((Character) ballonCharacterList[i]);
	            }
	            else {
	                isChecked = false;
	            }
	        }
	        if(isChecked) {
	            count ++;
	        }

	    }
	    return count;
    }
    """
    map_of_ranks = {}
    reporting_soldiers = 0

    for rank in ranks:
        if map_of_ranks.get(rank):
            map_of_ranks[rank] = map_of_ranks[rank] + 1
        else:
            map_of_ranks[rank] = 1

    for rank in map_of_ranks:
        higher_rank = rank + 1
        if map_of_ranks.get(higher_rank):
            reporting_soldiers += map_of_ranks[rank]
    return reporting_soldiers

def split(word):
    return [char for char in word]

def solution(S):
    list_of_string = split(S)






if __name__ == "__main__":
    print(solution([3,4,3,2,3,0]))
