from clause_in_wcnf_form import WCNF_Clauses
from maxsat_solver import Maxsat_Solver
from random_relationship_generator import init_graph_mfriend
import sys

if __name__ == "__main__":
    ## random generate a frined relationship, using for run time test
    graph = init_graph_mfriend(int(sys.argv[1]))
    
    ##Construct solver and .wcnf file
    clauses = WCNF_Clauses()
    clauses.build_clique_wcnf(graph)
    solver = Maxsat_Solver(clauses.wcnf_fname)
    solver.solve()
    
    ## Showing the result
    if solver.solved == False:
       ## A graph at least has clique with size 2
       print ("This is is not a graph")
    else:
        print ("The size of Max clique is", str(solver.solution.count(True)))
        for i in range(len(solver.solution)):
            if solver.solution[i] == True:
                print (i+1)
        
    ## delete tmp file        
    solver.delete_out_file()
   