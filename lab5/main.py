import copy

class CSPSolver:
    def __init__(self, graph, colors):
        self.graph = graph
        self.colors = colors
        self.domains = {node: list(colors) for node in graph}
        self.assignment = {} 

    def degree_heuristic(self):  #odlucuje koga bojimo
        """
        Bira neodeljenu promenljivu koja ima najviše ograničenja
        sa drugim NEODELJENIM promenljivim (najviše neobojenih suseda).
        """
        unassigned_nodes = [n for n in self.graph if n not in self.assignment]
        
        best_node = None
        max_degree = -1

        for node in unassigned_nodes:
            degree = 0
            for neighbor in self.graph[node]:
                if neighbor not in self.assignment:
                    degree += 1
            
            if degree > max_degree:
                max_degree = degree
                best_node = node

            elif degree == max_degree:
                 if best_node is None or node < best_node:
                     best_node = node
                     
        return best_node

    def forward_checking(self, var, color, current_domains): #nakon heur, smanjujemo domene susedima
        new_domains = copy.deepcopy(current_domains)
        
        neighbors = self.graph[var]
        
        for neighbor in neighbors:
            if neighbor not in self.assignment:
                if color in new_domains[neighbor]:
                    new_domains[neighbor].remove(color)
                    
                    if len(new_domains[neighbor]) == 0:
                        return None 
                        
        return new_domains

    def backtrack(self, domains):
        if len(self.assignment) == len(self.graph):
            return self.assignment

        var = self.degree_heuristic()

        for color in domains[var]:
            
            new_domains = self.forward_checking(var, color, domains)
            
            if new_domains is not None:
                self.assignment[var] = color
                
                result = self.backtrack(new_domains)
                if result is not None:
                    return result
                
                del self.assignment[var]
        
        return None

    def solve(self):
        return self.backtrack(self.domains)


australia_map = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'Q', 'SA'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q':  ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V':  ['SA', 'NSW'],
    'T':  [] 
}

available_colors = ['Red', 'Green', 'Blue']

solver = CSPSolver(australia_map, available_colors)
solution = solver.solve()

print("--- REŠENJE (Backtracking + FC + Degree Heuristic) ---")
if solution:
    for region, color in sorted(solution.items()):
        print(f"{region}: {color}")
else:
    print("Nema rešenja!")