<script lang="ts">
	import '../app.postcss';
	import { AppShell, AppBar } from '@skeletonlabs/skeleton';
</script>

<!-- App Shell -->
<AppShell>
	<svelte:fragment slot="header">
		<!-- App Bar -->
		<AppBar>
			<svelte:fragment slot="lead">
				<strong class="text-xl uppercase">KGSV Quiz</strong>
			</svelte:fragment>
			<svelte:fragment slot="trail">
				<a
					class="btn btn-sm variant-ghost-surface"
					href="./src/routes/login/login.svelte"
					target="_self"
					rel="noreferrer"
				>
					Log In
				</a>
				<a
					class="btn btn-sm variant-ghost-surface"
					href="./src/routes/login/register.svelte"
					target="_self"
					rel="noreferrer"
				>
					Sign Up
				</a>

			</svelte:fragment>
		</AppBar>
	</svelte:fragment>
	<!-- Page Route Content -->
	<slot />
</AppShell>
