"""
Removes all the redlinks from
a PIG datastructure.

Red links are defined by 
having 'only' one match per
the whole datastructure. these
are considered deadlinks and 
can be removed

"""
from org.apache.pig.scripting import * 

P = Pig.compile("""
	d = load 'data/wikilinks' as (url:chararray, pagerank:float, links:{link:(url:chararray)});
	d1 = foreach d generate url as from, flatten(links) as to;

	-- make sure the destination link
	-- is found

	d2 = filter d1 by to in $members;
	store d2 into 'out/wikilinks_redlinks';
""")

if __name__ == '__main__':
	members = open("./data/wikilinks.members", "r+").read()
	bound = P.bind({ 'members': members })
	bound.runSingle()	
