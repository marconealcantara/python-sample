import subprocess
import sys

def run_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar: {command}\n{e.stderr}")
        sys.exit(1)

def get_latest_tag(image_name):
    command = f'docker images {image_name} --format "{{{{.Tag}}}}"'
    tags = run_command(command).split('\n')
    tags = [tag for tag in tags if tag != "<none>" and tag != "latest"]
    if not tags:
        return None
    return sorted(tags)[-1]

def increment_tag(tag):
    if not tag:
        return "1.0.0"  # Começa em 1.0.0
    parts = tag.split('.')
    if parts[-1].isdigit():
        parts[-1] = str(int(parts[-1]) + 1)
    else:
        parts.append("1")
    return '.'.join(parts)

def build_and_push(image_name, dockerfile_path, context_dir):
    print(f"Construindo imagem {image_name}...")

    latest_tag = get_latest_tag(image_name)
    new_tag = increment_tag(latest_tag)

    incremental_image_tag = f"{image_name}:{new_tag}"
    latest_image_tag = f"{image_name}:latest"

    # Build com tag incremental
    build_command = f"docker build -t {incremental_image_tag} -f {dockerfile_path} {context_dir}"
    run_command(build_command)
    print(f"Imagem buildada com tag incremental: {new_tag}")

    # Tag latest para a mesma imagem incremental
    tag_latest_command = f"docker tag {incremental_image_tag} {latest_image_tag}"
    run_command(tag_latest_command)
    print(f"Tag 'latest' criada.")

    # Push incremental
    print(f"Fazendo push da imagem {incremental_image_tag} para Docker Hub...")
    run_command(f"docker push {incremental_image_tag}")

    # Push latest
    run_command(f"docker push {latest_image_tag}")

    print("Push realizado com sucesso para as tags:", new_tag, "e latest")

def main():
    dockerhub_user = "marconealcantara"

    backend_image  = f"{dockerhub_user}/backend"
    frontend_image = f"{dockerhub_user}/frontend"
    database_image = f"{dockerhub_user}/database"

    backend_dockerfile  = "./backend/Dockerfile"
    frontend_dockerfile = "./frontend/Dockerfile"
    database_dockerfile = "./database/Dockerfile"

    backend_context  = "./backend"
    frontend_context = "./frontend"
    database_context = "./database"

    print("Pipeline Backend")
    build_and_push(backend_image, backend_dockerfile, backend_context)

    print("\nPipeline Frontend")
    build_and_push(frontend_image, frontend_dockerfile, frontend_context)

    print("\nPipeline Database")
    build_and_push(database_image, database_dockerfile, database_context)

    # Comando helmfile apply na pasta ./helm/prod
    print("\nExecutando 'helmfile apply'...")
    run_command("helmfile -f ./helm/prod/helmfile.yaml apply")

if __name__ == "__main__":
    main()
