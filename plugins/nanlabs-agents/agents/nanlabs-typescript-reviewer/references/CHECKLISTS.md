# TypeScript review checklist

- [ ] No unjustified `any`
- [ ] External input parsed with `unknown` and validated
- [ ] Discriminated unions for variant state
- [ ] Exhaustive switch on discriminant
- [ ] Public exports have explicit or well-inferred types
- [ ] Async errors typed (not bare `catch (e)` without narrowing)
- [ ] Generic constraints preserve relationships
- [ ] No duplicate incompatible types for same domain concept
