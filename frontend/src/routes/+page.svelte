<!-- YOU CAN DELETE EVERYTHING IN THIS PAGE -->

<div class="container h-full mx-auto flex justify-center items-center">
	<div class="space-y-10 text-center flex flex-col items-center">
		<h2 class="h2">Welcome to our quiz!</h2>

		<a
					class="btn btn-xl variant-ghost-surface"
					href="./src/routes/quiz/questions.svelte"
					target="_self"
					rel="noreferrer"
					
				>
					Start New Game
		</a>

		<a
					class="btn btn-lg variant-ghost-surface"
					href="./src/routes/high-scores/high_scores.svelte"
					target="_self"
					rel="noreferrer"
				>
					Leaderboards
				</a>

		<a
					class="btn btn-lg variant-ghost-surface"
					href="./src/routes/how-to-play/how_to_play.svelte"
					target="_self"
					rel="noreferrer"
				>
					How to play
		</a>
	</div>
</div>

<style lang="postcss">
	figure {
		@apply flex relative flex-col;
	}
	figure svg,
	.img-bg {
		@apply w-64 h-64 md:w-80 md:h-80;
	}
	.img-bg {
		@apply absolute z-[-1] rounded-full blur-[50px] transition-all;
		animation: pulse 5s cubic-bezier(0, 0, 0, 0.5) infinite,
			glow 5s linear infinite;
	}
	@keyframes glow {
		0% {
			@apply bg-primary-400/50;
		}
		33% {
			@apply bg-secondary-400/50;
		}
		66% {
			@apply bg-tertiary-400/50;
		}
		100% {
			@apply bg-primary-400/50;
		}
	}
	@keyframes pulse {
		50% {
			transform: scale(1.5);
		}
	}
</style>
