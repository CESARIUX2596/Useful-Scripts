import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import torchvision.models as models
import matplotlib.pyplot as plt
import numpy as np
import random
import os


def load_dataset():
    # Set dataset path
    dataset_path = "./data/cifar10"

    transform_train = transforms.Compose(
        [
            transforms.RandomCrop(32, padding=4),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
        ]
    )

    transform_test = transforms.Compose(
        [
            transforms.ToTensor(),
            transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
        ]
    )

    # Load CIFAR-10 dataset
    trainset = torchvision.datasets.CIFAR10(
        root=dataset_path, train=True, download=True, transform=transform_train
    )
    trainloader = torch.utils.data.DataLoader(
        trainset, batch_size=2048, shuffle=True, num_workers=2
    )

    testset = torchvision.datasets.CIFAR10(
        root=dataset_path, train=False, download=True, transform=transform_test
    )
    testloader = torch.utils.data.DataLoader(
        testset, batch_size=32, shuffle=False, num_workers=2
    )

    # Class names for CIFAR-10 dataset
    classes = (
        "plane",
        "car",
        "bird",
        "cat",
        "deer",
        "dog",
        "frog",
        "horse",
        "ship",
        "truck",
    )

    return trainset, trainloader, testset, testloader, classes


def train(model, trainloader, criterion, optimizer, device):
    train_loss = 0.0
    train_total = 0
    train_correct = 0

    # Switch to train mode
    model.train()

    for inputs, labels in trainloader:
        inputs, labels = inputs.to(device), labels.to(device)

        # Zero the parameter gradients
        optimizer.zero_grad()

        # Forward pass
        outputs = model(inputs)
        loss = criterion(outputs, labels)

        # Backward pass and optimize
        loss.backward()
        optimizer.step()

        # Update training loss
        train_loss += loss.item() * inputs.size(0)

        # Compute training accuracy
        _, predicted = torch.max(outputs, 1)
        train_total += labels.size(0)
        train_correct += (predicted == labels).sum().item()

    # Compute average training loss and accuracy
    train_loss = train_loss / len(trainloader.dataset)
    train_accuracy = 100.0 * train_correct / train_total

    return model, train_loss, train_accuracy


def test(model, testloader, criterion, device):
    test_loss = 0.0
    test_total = 0
    test_correct = 0

    # Switch to evaluation mode
    model.eval()

    with torch.no_grad():
        for inputs, labels in testloader:
            inputs, labels = inputs.to(device), labels.to(device)

            # Forward pass
            outputs = model(inputs)
            loss = criterion(outputs, labels)

            # Update test loss
            test_loss += loss.item() * inputs.size(0)

            # Compute test accuracy
            _, predicted = torch.max(outputs, 1)
            test_total += labels.size(0)
            test_correct += (predicted == labels).sum().item()

    # Compute average test loss and accuracy
    test_loss = test_loss / len(testloader.dataset)
    test_accuracy = 100.0 * test_correct / test_total

    return test_loss, test_accuracy


def train_epochs(
    model,
    trainloader,
    testloader,
    criterion,
    optimizer,
    device,
    num_epochs,
    save_interval=5,
):
    train_losses = []
    train_accuracies = []
    test_losses = []
    test_accuracies = []

    for epoch in range(num_epochs):
        print(f"Epoch {epoch+1}/{num_epochs}")
        model, train_loss, train_accuracy = train(
            model, trainloader, criterion, optimizer, device
        )
        test_loss, test_accuracy = test(model, testloader, criterion, device)

        train_losses.append(train_loss)
        train_accuracies.append(train_accuracy)
        test_losses.append(test_loss)
        test_accuracies.append(test_accuracy)

        print(f"Train Loss: {train_loss:.4f} - Train Accuracy: {train_accuracy:.2f}%")
        print(f"Test Loss: {test_loss:.4f} - Test Accuracy: {test_accuracy:.2f}%")
        print()

        if (epoch + 1) % save_interval == 0:
            # Save the model and variables
            torch.save(model.state_dict(), f"./models/resnet50_cifar10_{epoch+1}.pth")
            checkpoint = {
                "epoch": epoch + 1,
                "train_losses": train_losses,
                "train_accuracies": train_accuracies,
                "test_losses": test_losses,
                "test_accuracies": test_accuracies,
                "classes": classes,
            }
            torch.save(checkpoint, f"./models/resnet50_cifar10_variables_{epoch+1}.pth")

    return model, train_losses, train_accuracies, test_losses, test_accuracies


def plot_loss(train_losses, test_losses):
    plt.figure()
    plt.plot(range(len(train_losses)), train_losses, label="Training Loss")
    plt.plot(range(len(test_losses)), test_losses, label="Validation Loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()
    plt.savefig("loss_plot.png")
    # plt.show()


def plot_accuracy(train_accuracies, test_accuracies):
    plt.figure()
    plt.plot(range(len(train_accuracies)), train_accuracies, label="Training Accuracy")
    plt.plot(range(len(test_accuracies)), test_accuracies, label="Validation Accuracy")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.savefig("accuracy_plot.png")
    # plt.show()


def plot_image(dataset, model, classes):
    idx = random.randint(0, len(dataset))
    label = dataset[idx][1]
    img = (
        dataset[idx][0].unsqueeze(0).to(device)
    )  # Move the input image tensor to the GPU
    model.eval()
    # model.to(device)  # Move the model to the GPU
    output = model(img)
    _, predicted = torch.max(output.data, 1)
    # Convert the image and show it
    img = (
        img.squeeze().permute(1, 2, 0).cpu()
    )  # Move the image tensor back to the CPU and adjust dimensions
    plt.imshow(img)
    plt.axis("off")
    plt.title(f"Predicted: {classes[predicted]}, True: {classes[label]}")
    plt.savefig("predicted_image.png")
    # plt.show()
    print("Predicted label: ", classes[predicted[0].item()])
    print("Actual label: ", classes[label])


if __name__ == "__main__":
    # Flag to control whether to run training or use saved fine-tuned model.
    train_model = True

    # Create a directory to save the models
    if not os.path.exists("./models"):
        os.makedirs("./models")

    # Set random seed for reproducibility
    random_seed = 1313
    torch.manual_seed(random_seed)
    np.random.seed(random_seed)
    random.seed(random_seed)

    # Number of classes
    num_classes = 10

    # Import ResNet50 model pretrained on ImageNet
    model = models.resnet50(pretrained=True)
    print("Network before modifying conv1:")
    print(model)

    # Modify conv1 to suit CIFAR-10
    model.conv1 = nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1, bias=False)

    # Modify the final fully connected layer according to the number of classes
    num_features = model.fc.in_features
    model.fc = nn.Linear(num_features, num_classes)
    print("Network after modifying conv1:")
    print(model)

    # Move the model to GPU if available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)

    # Define loss function and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9, weight_decay=5e-4)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=200)

    # Load the dataset
    trainset, trainloader, testset, testloader, classes = load_dataset()

    if train_model:
        # Train the model for 20 epochs, saving every 5 epochs
        num_epochs = 60
        save_interval = 5
        model, train_losses, train_accuracies, test_losses, test_accuracies = (
            train_epochs(
                model,
                trainloader,
                testloader,
                criterion,
                optimizer,
                device,
                num_epochs,
                save_interval,
            )
        )

        # Save the final trained model
        torch.save(
            model.state_dict(),
            f"./models/resnet50_cifar10_final_model_epochs_{num_epochs}.pth",
        )

        # Plot and save the loss and accuracy plots
        plot_loss(train_losses, test_losses)
        plot_accuracy(train_accuracies, test_accuracies)
    else:
        # Load the pre-trained model
        model.load_state_dict(
            torch.load("./models/resnet50_cifar10_final_model_epochs_50.pth")
        )
        # Load the variables
        checkpoint = torch.load("./models/resnet50_cifar10_variables.pth")
        epoch = checkpoint["epoch"]
        train_losses = checkpoint["train_losses"]
        train_accuracies = checkpoint["train_accuracies"]
        test_losses = checkpoint["test_losses"]
        test_accuracies = checkpoint["test_accuracies"]
        classes = checkpoint["classes"]
        model.to(device)
        model.eval()

    # Plot and save an example image
    plot_image(testset, model, classes)
