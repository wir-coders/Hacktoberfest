import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;

public class Construction {

	private class Vertex
	{
		HashMap<String,Integer> nbrs=new HashMap<>();
	}
	HashMap<String,Vertex> vtces;
	public Construction()
	{
		vtces=new HashMap<>();
	}
	
	public int numVertex()
	{
		return this.vtces.size();
	}
	
	public boolean containVertex(String vname)
	{
		return this.vtces.containsKey(vname);
	}
	
	public void addVertex(String vname)
	{
		Vertex vtc=new Vertex();
		this.vtces.put(vname, vtc);
	}
	
	public void removeVertex(String vname)
	{
		if(!this.containVertex(vname))
			return;
		Vertex vtc=this.vtces.get(vname);
		ArrayList<String> keys=new ArrayList<>(vtc.nbrs.keySet());
		for(String key:keys)
		{
			Vertex nbrvtc=this.vtces.get(key);
			nbrvtc.nbrs.remove(vname);
		}
		vtces.remove(vname);
	}
	
	public int numEdge()
	{
		ArrayList<String> arr=new ArrayList<>(this.vtces.keySet());
		int res=0;
		for(String a:arr)
		{
			Vertex vtc=this.vtces.get(a);
			res+=vtc.nbrs.size();
		}
		return res/2;
			
	}
	
	public boolean containEdge(String vname1,String vname2)
	{

		Vertex vtc1=this.vtces.get(vname1);
		Vertex vtc2=this.vtces.get(vname2);
		if(vtc1==null || vtc2==null || !vtc1.nbrs.containsKey(vname2))
			return false;
		return true;
	}
	
	public void addEdge(String vname1,String vname2,int cost)					//this function create edge only for pre-existing vertex
	{

		Vertex vtc1=this.vtces.get(vname1);
		Vertex vtc2=this.vtces.get(vname2);
		if(vtc1==null || vtc2==null || vtc1.nbrs.containsKey(vname2))
			return ;
		vtc1.nbrs.put(vname2, cost);
		vtc2.nbrs.put(vname1, cost);
	}
	
	public void removeEdge(String vname1,String vname2)
	{
		Vertex vtc1=this.vtces.get(vname1);
		Vertex vtc2=this.vtces.get(vname2);
		if(vtc1==null || vtc2==null || !vtc1.nbrs.containsKey(vname2))
			return ;
		vtc1.nbrs.remove(vname2);
		vtc2.nbrs.remove(vname1);		
	}
	
	public void display()
	{
		System.out.println("---------------------------------------------------------");
		if(vtces.size()==0)
			return;
		ArrayList<String> keys=new ArrayList<>(this.vtces.keySet());
		for(String key:keys)
		{
			Vertex vtc=this.vtces.get(key);
			System.out.println(key+":"+vtc.nbrs);
		}
		System.out.println("---------------------------------------------------------");
	}
	
	
	
	
	public boolean hasPath(String vname1,String vname2)
	{
		return this.hasPath(vname1, vname2, new HashMap<>());
	}
	public boolean hasPath(String vname1,String vname2,HashMap<String,Boolean> processed)
	{
		processed.put(vname1, true);
		if(this.containEdge(vname1, vname2))
			return true;
		Vertex vtc=this.vtces.get(vname1);
		if(vtc==null)
			return false;
		ArrayList<String> keys=new ArrayList<>(vtc.nbrs.keySet());
		for(String key:keys)
		{
			if(!processed.containsKey(key) && hasPath(key,vname2,processed))
				return true;
		}
		return false;
	}
	
	
	
	
	
	
	
	
	
	
	
	////////////												Breadth First Search                    ///////////////////////
	private class Pair{
		String vname;
		String psf;
	}
	public boolean bfs(String src,String dst)
	{
		HashMap<String,Boolean> processed=new HashMap<>();
		LinkedList<Pair> queue=new LinkedList<>();
		Pair p=new Pair();
		p.vname=src;
		p.psf=src;
		queue.addLast(p);
		while(!queue.isEmpty())
		{
			Pair rmv=queue.removeFirst();
			if(processed.containsKey(rmv.vname))
				continue;
			processed.put(rmv.vname, true);
			if(this.containEdge(rmv.vname, dst))
			{
				System.out.println(rmv.psf+dst);
				return true;
			}
			Vertex vtc=this.vtces.get(rmv.vname);
			ArrayList<String> nbrs=new ArrayList<>(vtc.nbrs.keySet());
			for(String nbr:nbrs)
			{
				if(!processed.containsKey(nbr))
				{
					Pair ad=new Pair();
					ad.vname=nbr;
					ad.psf=rmv.psf+nbr;
					queue.addLast(ad);
				}
			}
		}
		return false;
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
		///////////////										Depth First Search                              //////////////////
	public boolean dfs(String src,String dst)
	{
		HashMap<String,Boolean> processed=new HashMap<>();
		LinkedList<Pair> stack=new LinkedList<>();
		Pair p=new Pair();
		p.vname=src;
		p.psf=src;
		stack.addFirst(p);
		while(!stack.isEmpty())
		{
			Pair rmv=stack.removeFirst();
			if(processed.containsKey(rmv.vname))
				continue;
			processed.put(rmv.vname, true);
			if(this.containEdge(rmv.vname, dst))
			{
				System.out.println(rmv.psf+dst);
				return true;
			}
			Vertex vtc=this.vtces.get(rmv.vname);
			ArrayList<String> nbrs=new ArrayList<>(vtc.nbrs.keySet());
			for(String nbr:nbrs)
			{
				if(!processed.containsKey(nbr))
				{
					Pair ad=new Pair();
					ad.vname=nbr;
					ad.psf=rmv.psf+nbr;
					stack.addFirst(ad);
				}
			}
		}
		return false;
	}
	
	
	
	
	
	
	
	
	
	
	
	////////////												Breadth First Traversal                    ///////////////////////
	public void bft()
	{
		HashMap<String,Boolean> processed=new HashMap<>();
		LinkedList<Pair> queue=new LinkedList<>();
		Pair p=new Pair();
		ArrayList<String> arr=new ArrayList<>(this.vtces.keySet());
		for(String key:arr)
		{
			if(processed.containsKey(key))
				continue;
			p.vname=key;
			p.psf=key;
			queue.addLast(p);
			while(!queue.isEmpty())
				{
					Pair rmv=queue.removeFirst();
					if(processed.containsKey(rmv.vname))
						continue;
					processed.put(rmv.vname, true);
					System.out.println(rmv.vname+" via "+rmv.psf);
					Vertex vtc=this.vtces.get(rmv.vname);
					ArrayList<String> nbrs=new ArrayList<>(vtc.nbrs.keySet());
					for(String nbr:nbrs)
						{
							if(!processed.containsKey(nbr))
								{
									Pair ad=new Pair();
									ad.vname=nbr;
									ad.psf=rmv.psf+nbr;
									queue.addLast(ad);
								}
						}
					}
			}
	}	
	
	
	
	
	
	
	
	
	
	
	
	
	///////////////											Depth First Traversal                            //////////////////
	public void dft()
	{
		HashMap<String,Boolean> processed=new HashMap<>();
		LinkedList<Pair> stack=new LinkedList<>();
		Pair p=new Pair();
		ArrayList<String> arr=new ArrayList<>(this.vtces.keySet());
		for(String key:arr)
		{
			if(processed.containsKey(key))
				continue;
			p.vname=key;
			p.psf=key;
			stack.addFirst(p);
			while(!stack.isEmpty())
				{
					Pair rmv=stack.removeFirst();
					if(processed.containsKey(rmv.vname))
						continue;
					processed.put(rmv.vname, true);
					System.out.println(rmv.vname+" via "+rmv.psf);
					Vertex vtc=this.vtces.get(rmv.vname);
					ArrayList<String> nbrs=new ArrayList<>(vtc.nbrs.keySet());
					for(String nbr:nbrs)
						{
							if(!processed.containsKey(nbr))
								{
									Pair ad=new Pair();
									ad.vname=nbr;
									ad.psf=rmv.psf+nbr;
									stack.addFirst(ad);
								}
						}
					}
			}
	}	
	
	
	
	
	
	
	
	
	
	
	////////////////                    Is Cyclic by BFT								////////////////////////
	public boolean isCyclic()
	{
		HashMap<String,Boolean> processed=new HashMap<>();
		LinkedList<Pair> queue=new LinkedList<>();
		ArrayList<String> arr=new ArrayList<>(this.vtces.keySet());
		for(String key:arr)
		{
			if(processed.containsKey(key))
				continue;
			Pair p=new Pair();
			p.vname=key;
			p.psf=key;
			queue.addLast(p);
			while(!queue.isEmpty())
				{
					Pair rmv=queue.removeFirst();
					if(processed.containsKey(rmv.vname))
						return true;
					processed.put(rmv.vname, true);
					Vertex vtc=this.vtces.get(rmv.vname);
					ArrayList<String> nbrs=new ArrayList<>(vtc.nbrs.keySet());
					for(String nbr:nbrs)
						{
							if(!processed.containsKey(nbr))
								{
									Pair ad=new Pair();
									ad.vname=nbr;
									ad.psf=rmv.psf+nbr;
									queue.addLast(ad);
								}
						}
					}
			}
		return false;
	}	
	
	
	
	
	
	
	
	
	
	
	////////////												Is Connected Breadth First Traversal                    ///////////////////////
	public boolean isConnected()
	{
		int flag=0;
		HashMap<String,Boolean> processed=new HashMap<>();
		LinkedList<Pair> queue=new LinkedList<>();
		Pair p=new Pair();
		ArrayList<String> arr=new ArrayList<>(this.vtces.keySet());
		for(String key:arr)
		{
			if(processed.containsKey(key))
				continue;
			flag+=1;
			p.vname=key;
			p.psf=key;
			queue.addLast(p);
			while(!queue.isEmpty())
				{
					Pair rmv=queue.removeFirst();
					if(processed.containsKey(rmv.vname))
						continue;
					processed.put(rmv.vname, true);
					Vertex vtc=this.vtces.get(rmv.vname);
					ArrayList<String> nbrs=new ArrayList<>(vtc.nbrs.keySet());
					for(String nbr:nbrs)
						{
							if(!processed.containsKey(nbr))
								{
									Pair ad=new Pair();
									ad.vname=nbr;
									ad.psf=rmv.psf+nbr;
									queue.addLast(ad);
								}
						}
					}
			}
		if(flag>=2)												// basically flag signify the number of components present in graph
			return false;
		else
			return true;
	}	
	
	
	
	
	
	
	
	
	///////////////////////////                  Graph is a Tree or not                                /////////////////////////////
	public boolean isTree()
	{
		return !this.isCyclic()&&this.isConnected();
	}
	
	
	
	
	
	////////////////////////////            	 Get Connected Components                                ////////////////////////////////
	public ArrayList<ArrayList<String>> getConnectedComponents()
	{
		ArrayList<ArrayList<String>> res=new ArrayList<>();
		HashMap<String,Boolean> processed=new HashMap<>();
		LinkedList<Pair> queue=new LinkedList<>();
		Pair p=new Pair();
		ArrayList<String> arr=new ArrayList<>(this.vtces.keySet());
		for(String key:arr)
		{
			if(processed.containsKey(key))
				continue;
			ArrayList<String> component=new ArrayList<>();
			p.vname=key;
			p.psf=key;
			queue.addLast(p);
			while(!queue.isEmpty())
				{
					Pair rmv=queue.removeFirst();
					if(processed.containsKey(rmv.vname))
						continue;
					processed.put(rmv.vname, true);
					component.add(rmv.vname);
					Vertex vtc=this.vtces.get(rmv.vname);
					ArrayList<String> nbrs=new ArrayList<>(vtc.nbrs.keySet());
					for(String nbr:nbrs)
						{
							if(!processed.containsKey(nbr))
								{
									Pair ad=new Pair();
									ad.vname=nbr;
									ad.psf=rmv.psf+nbr;
									queue.addLast(ad);
								}
						}
					}
			res.add(component);
			}
		return res;
	}	
	
	
	
	
	
	
	
	
	///////////////////////                    Minimum Spanning Tree (Prims Approeach)             /////////////////////////////////
	
	public static void main(String[] args) {
		
		Construction nik=new Construction();
//		nik.addVertex("A");
//		nik.addVertex("B");
//		nik.addVertex("C");
//		nik.addVertex("D");
//		nik.addVertex("E");
//		nik.addVertex("F");
//		nik.addVertex("G");
//		
//		nik.addEdge("A", "B", 3);
//		nik.addEdge("A", "D", 2);
//		nik.addEdge("B", "C", 4);
//		nik.addEdge("C", "D", 7);
//		nik.addEdge("D", "E", 10);
//		nik.addEdge("E", "F", 9);
//		nik.addEdge("E", "G", 8);
//		nik.addEdge("F", "G", 6);
//		
//		nik.display();
//		System.out.println(nik.numVertex());
//		System.out.println(nik.numEdge());
//		System.out.println(nik.containEdge("A", "C"));
//		System.out.println(nik.containEdge("A", "B"));
//		nik.removeEdge("A", "B");
//		System.out.println();
//		nik.display();
//		nik.removeVertex("F");
//		System.out.println();
//		nik.display();
//		nik.addVertex("Z");
//		System.out.println();
//		nik.display();
//		nik.addEdge("A", "Z", 3);
//		System.out.println();
//		nik.display();
//		nik.addEdge("A", "Y", 1);   									
// 		nik.removeEdge("D", "E");
		
//		System.out.println(nik.hasPath("Q", "A"));
		
		
//		nik.removeEdge("A", "D");
//		System.out.println(nik.bfs("A", "F"));
		
		
		
		
		
		
//		nik.addVertex("A");
//		nik.addVertex("H");
//		nik.addVertex("C");
//		nik.addVertex("D");
//		nik.addVertex("E");
//		nik.addVertex("F");
//		nik.addVertex("G");
//		
//		nik.addEdge("A", "H", 3);
//		nik.addEdge("A", "D", 2);
//		nik.addEdge("H", "C", 4);
//		nik.addEdge("C", "D", 7);
//		nik.addEdge("D", "E", 10);
//		nik.addEdge("E", "F", 9);
//		nik.addEdge("E", "G", 8);
//		nik.addEdge("F", "G", 6);
//		nik.display();
//		System.out.println(nik.dfs("A", "G"));
		
		
		
		
		
//		nik.addVertex("A");
//		nik.addVertex("B");
//		nik.addVertex("C");
//		nik.addVertex("D");
//		nik.addVertex("E");
//		nik.addVertex("F");
//		nik.addVertex("G");
//		
//		nik.addEdge("A", "B", 3);
//		nik.addEdge("A", "D", 2);
//		nik.addEdge("B", "C", 4);
//		nik.addEdge("C", "D", 7);
//		nik.addEdge("D", "E", 10);
//		nik.addEdge("E", "F", 9);
//		nik.addEdge("E", "G", 8);
//		nik.addEdge("F", "G", 6);
//		
//		nik.removeEdge("D", "E");
//		nik.bft();
//		
		
		

		
//		nik.addVertex("A");
//		nik.addVertex("B");
//		nik.addVertex("C");
//		nik.addVertex("D");
//		nik.addVertex("E");
//		nik.addVertex("F");
//		nik.addVertex("G");
//		
//		nik.addEdge("A", "B", 3);
//		nik.addEdge("A", "D", 2);
//		nik.addEdge("B", "C", 4);
//		nik.addEdge("C", "D", 7);
//		nik.addEdge("D", "E", 10);
//		nik.addEdge("E", "F", 9);
//		nik.addEdge("E", "G", 8);
//		nik.addEdge("F", "G", 6);
//		
//		nik.removeEdge("D", "E");
//		nik.dft();
		
		
		
		
//		nik.addVertex("A");
//		nik.addVertex("B");
//		nik.addVertex("C");
//		nik.addVertex("D");
//		nik.addVertex("E");
//		nik.addVertex("F");
//		nik.addVertex("G");
//		
//		nik.addEdge("A", "B", 3);
//		nik.addEdge("A", "D", 2);
//		nik.addEdge("B", "C", 4);
//		nik.addEdge("C", "D", 7);
//		nik.addEdge("D", "E", 10);
//		nik.addEdge("E", "F", 9);
//		nik.addEdge("E", "G", 8);
//		nik.addEdge("F", "G", 6);
//		nik.removeEdge("B", "C");
//		nik.removeEdge("F", "G");
//		nik.display();
//		System.out.println(nik.isCyclic());
		
		
		
//		nik.addVertex("A");
//		nik.addVertex("B");
//		nik.addVertex("C");
//		nik.addVertex("D");
//		nik.addVertex("E");
//		nik.addVertex("F");
//		nik.addVertex("G");
//		
//		nik.addEdge("A", "B", 3);
//		nik.addEdge("A", "D", 2);
//		nik.addEdge("B", "C", 4);
//		nik.addEdge("C", "D", 7);
//		nik.addEdge("D", "E", 10);
//		nik.addEdge("E", "F", 9);
//		nik.addEdge("E", "G", 8);
//		nik.addEdge("F", "G", 6);
//		
//		nik.display();
//		nik.removeEdge("D", "E");
//		System.out.println(nik.isConnected());
		
		
		
		
		
		
		
//
//		nik.addVertex("A");
//		nik.addVertex("B");
//		nik.addVertex("C");
//		nik.addVertex("D");
//		nik.addVertex("E");
//		nik.addVertex("F");
//		nik.addVertex("G");
//		
//		nik.addEdge("A", "B", 3);
//		nik.addEdge("A", "D", 2);
//		nik.addEdge("B", "C", 4);
//		nik.addEdge("C", "D", 7);
//		nik.addEdge("D", "E", 10);
//		nik.addEdge("E", "F", 9);
//		nik.addEdge("E", "G", 8);
//		nik.addEdge("F", "G", 6);
		
//		nik.display();
//		nik.removeEdge("B", "C");
//		nik.removeEdge("F", "G");
//		nik.removeEdge("D", "E");
//		System.out.println(nik.isTree());
		
		
		
		
		
		
		
		

		nik.addVertex("A");
		nik.addVertex("B");
		nik.addVertex("C");
		nik.addVertex("D");
		nik.addVertex("E");
		nik.addVertex("F");
		nik.addVertex("G");
		
		nik.addEdge("A", "B", 3);
		nik.addEdge("A", "D", 2);
		nik.addEdge("B", "C", 4);
		nik.addEdge("C", "D", 7);
		nik.addEdge("D", "E", 10);
		nik.addEdge("E", "F", 9);
		nik.addEdge("E", "G", 8);
		nik.addEdge("F", "G", 6);
		nik.removeEdge("D", "E");
		nik.addVertex("H");
		System.out.println(nik.getConnectedComponents());
	}

}
