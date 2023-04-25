# layout/optimize.jl

function foo(N::Integer, d::AbstractVector{<:Integer})
	a = zeros(sum(d)+1)
	j = 1
	p = Vector{Int}(undef, N)
	for i = 1:N
		a[j] += inv(i)
		p[i] = j
		d[i] == 1 && (j += 1)
	end
	bp = sum((1:N) .* a[p] .^ 2)
	bm = sum(inv.((1:N) .* a[p] .^ 2))
	return a[p], bp, bm
end

evaluate_target(N::Integer, d::AbstractVector{<:Integer}) = 
	2 * sqrt(prod(foo(N, d)[2:3]))

function find_best_cut(N::Integer=18)
	dd = digits.(0 : 1<<(N-1) - 1; base=2, pad=N)
	target, i = findmin(evaluate_target.(N, dd))
	return target / N - 2, dd[i]
end

function optimize_layout(N::Integer=18)
	score, d = find_best_cut(N)
	a, bp, bm = foo(N, d)
	s = sqrt(bm / bp)
	return s .* a, inv.(1:N) ./ a
end

heights, widths = optimize_layout(18)

function print_scheme(dimensions, heights)
	for i = eachindex(heights)
		print(dimensions[i], 
			i < length(heights) && heights[i] == heights[i+1] ? ' ' : '\n')
	end
end

Q = 200

print_scheme(diff([0; round.(Int, cumsum(widths .* Q))]), heights)
# 200
# 120 80
# 81 65 54
# 75 66 59
# 57 52 47 44
# 45 43 39 38 35

print_scheme(round.(Int, heights .* Q), heights)
# 135
# 113 113
# 84 84 84
# 51 51 51
# 48 48 48 48
# 43 43 43 43 43

[0; cumsum(unique(round.(Int, heights .* Q)))]
# 0
# 135
# 248
# 332
# 383
# 431
# 474
